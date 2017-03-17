#-*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from prontuario.models import *

from prontuario.forms import *

from django.db import connection, transaction

#from datetime import date
from datetime import datetime
from django.utils import timezone

@login_required
def home(request):
	hj = timezone.now()
	user = request.user.id
	pacientes = Paciente.objects.all();
	form = ConsultaForm(request.POST or None)
	tipo_profissional = TipoProfissional.objects.all()

	consultas_do_dia = Consultas.objects.all().filter(data=hj)


	context = {
		'user': user,
		'pacientes': pacientes,
		'tipo_profissional': tipo_profissional,
		'form': form,
		'consultas_do_dia': consultas_do_dia,
		'hj': hj
	}

	return render(request, 'prontuario/home.html', context)

def nada(request):
	return redirect('home')


@login_required
def consulta(request):
	consultas = Consultas.objects.all()

	return render(request, 'prontuario/consulta.html', {'consultas' : consultas})

def filtrar_consulta(request):
	c1 = None
	if 'data_inicio' in request.GET:
		c1 = Consultas.objects.filter(data__range=(request.GET['data_inicio'], request.GET['data_final']))
	context = {
		'consultas': c1,
	}
	return render(request, 'prontuario/filtrar_consulta.html', context)
	# return render(request, 'prontuario/filtrar_consulta.html')

def consulta_create(request):
	form = ConsultaForm(request.POST or None)
	return render(request, 'prontuario/consulta_create.html', {'form': form})	

def abrir_consulta(request):
	if request.method == 'POST':
		form = ConsultaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
		form = ConsultaForm()
	
	return render(request, 'prontuario/consulta_create.html', {'form' : form})

def consulta_do_dia(request):

	now = datetime.now()

	consultas_dia = Consultas.objects.filter(data=now)

	# c[1].get_paciente()

	cursor1 = connection.cursor()

	cursor1.execute("select c.id, c.data, c.hora, cp.profissional_id, p.nome, p.tipo_id from prontuario_consultas as c " 
		+ "inner join prontuario_consultas_profissionais as cp on c.id=cp.consultas_id " 
		+ "inner join prontuario_profissional as p on cp.profissional_id=p.id " 
		+ "where c.data=date('now')")

	c_abertas = cursor1.fetchall()

	context = {
		'c_abertas': c_abertas,
		'consultas_dia': consultas_dia,
	}


	return render(request, 'prontuario/consulta_do_dia.html', context)

@login_required
def tabela(request):
	return render(request, 'prontuario/tabela.html')

@login_required
def tipo_profissional(request):
	pass

@login_required
def editar_paciente(request, id_paciente):
	paciente = Paciente.objects.get(id=id_paciente)
	pacientes = Paciente.objects.all();
	
@login_required
def excluir_paciente(request, id_paciente):
	paciente = Paciente.objects.get(id=id_paciente)
	paciente.delete()
	#return HttpResponseRedirect('prontuario/home.html')
	
def do_logout(request):
	logout(request)
	return redirect('login')

def do_login(request):
	tipo_profissional = TipoProfissional.objects.all()
	error = False
	if request.method == 'POST':
		context = {
			'error': error
		}
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			error = True
			login(request, user)
			return redirect('home')
		else:
			error = False
	context = {
		'error': error,
		'tipo_profissional': tipo_profissional
	}
	return render(request, 'prontuario/login.html', context)

def endereco_create(request):
	if request.method == 'POST':
		form = EnderecoForm(request.POST)
		if form.is_valid():
			endereco = Endereco()
			endereco.rua = form.cleaned_data['rua']
			endereco.numero = form.cleaned_data['numero']
			endereco.bairro = form.cleaned_data['bairro']
			endereco.cep = form.cleaned_data['cep']
			endereco.cidade = form.cleaned_data['cidade']
			endereco.estado = form.cleaned_data['estado']
			endereco.save()

			return redirect('endereco_create')

	else:
		form = EnderecoForm()
	
	return render(request, 'prontuario/post_create.html', {'form' : form})

# def consulta_create(request):
# 	#paciente = Paciente.objects.get(id=id_paciente)

# 	if request.method == 'POST':
# 		form = ConsultaForm(request.POST)
# 		#form = ConsultaForm(request.POST or None, instance=paciente)
# 		if form.is_valid():
# 			consulta = Consultas()
# 			consulta.data = form.cleaned_data['data']
# 			consulta.profissionais = form.cleaned_data['profissionais']
# 			consulta.paciente = form.cleaned_data['paciente']
# 			endereco.save()

# 			return redirect('home')

# 	else:
# 		form = ConsultaForm()
	
# 	return render(request, 'prontuario/home.html', {'form' : form})

def paciente_create(request):
	if request.method == 'POST':
		form = PacienteForm(request.POST)
		if form.is_valid():
			paciente = Paciente()
			paciente.nome = form.cleaned_data['nome']
			paciente.sexo = form.cleaned_data['sexo']
			paciente.cpf = form.cleaned_data['cpf']
			paciente.rg = form.cleaned_data['rg']
			paciente.telefone = form.cleaned_data['telefone']
			paciente.nascimento = form.cleaned_data['nascimento']
			paciente.sus = form.cleaned_data['sus']
			paciente.responsavel = form.cleaned_data['responsavel']
			paciente.familia = form.cleaned_data['familia']
			paciente.save()

			return redirect('endereco_create')

	else:
		form = EnderecoForm()
	
	return render(request, 'prontuario/post_create.html', {'form' : form})


def consulta_update(request):
	paciente = str(request.GET.get('id_paciente'))
	consulta = str(request.GET.get('id_consulta'))

	
	cursor2 = connection.cursor()

	cursor2.execute("select count(*) from prontuario_consultas_paciente where paciente_id=%s and consultas_id=%s" % (paciente, consulta))	
	verificar_existe_paciente = cursor2.fetchall()

	if verificar_existe_paciente[0][0] == 0:	
		if request.method == 'GET':
			cursor1 = connection.cursor()


			cursor1.execute("insert into prontuario_consultas_paciente (consultas_id, paciente_id) " 
				+ "values (%s, %s)" % (consulta, paciente))

			#cursor1.fetchall()

			context = {
				'paciente': request.GET.get('id_consulta'),
				'consulta': request.GET.get('id_paciente'),
			}

			return redirect('home')
	else:
		return redirect('home')


@login_required
def visualizar_paciente(request, id_paciente):

	paciente = Paciente.objects.get(id=id_paciente)
	pacientes = Paciente.objects.all();
	#tipo_profissional = TipoProfissional.objects.all().exclude(nome='Agente de Saúde')
	cursor1 = connection.cursor()
	cursor2 = connection.cursor()
	cursor3 = connection.cursor()

	cursor1.execute("select f.num_prontuario from prontuario_paciente as p "  
		+ "inner join prontuario_familia as f on p.familia_id=f.id " 
		+ "where p.id=%s;" % id_paciente)

	num_prontuario = cursor1.fetchall()

	cursor2.execute("select count(t.id) as 'count', p.nome as 'nome_paciente', prof.nome as 'nome_prof' " 
		+ ", t.nome as 'nome_tipo' " 
		+ "from prontuario_consultas as c " 
		+ "inner join prontuario_consultas_paciente as cp on c.id=cp.consultas_id " 
		+ "inner join prontuario_paciente as p on cp.paciente_id=p.id " 
		+ "inner join prontuario_consultas_profissionais as  cprof on cprof.consultas_id=c.id " 
		+ "inner join prontuario_profissional as prof on cprof.profissional_id=prof.id " 
		+ "inner join prontuario_tipoprofissional as t on prof.tipo_id=t.id " 
		+ "inner join prontuario_familia as f on f.id=p.familia_id " 
		+ "where p.id=%s group by t.id;", [id_paciente])


	dados2 = cursor2.fetchall()

	linha = num_prontuario[0][0]
	#linha = ''.join(num_prontuario)
	#pegar o numero do prontuario que está na coluna 5
	#linha = dados[0][4]

	cursor3.execute("select num_prontuario, p.nome, p.responsavel from prontuario_familia as f " 
		+ "inner join prontuario_paciente as p on p.familia_id=f.id " 
		+ "where f.num_prontuario=%s order by p.responsavel desc;" % linha)

	dados3 = cursor3.fetchall()

	# Para atualizar o Paciente (aparece no form de edicao)
	form = PacienteForm(request.POST or None, instance=paciente)

	context = {
		'paciente': paciente,
		#'pacientes': pacientes,
		'form': form,
		'dados2': list(dados2),
		'dados3': list(dados3),
		'num': num_prontuario,
		'linha': linha,
	}

	if form.is_valid():
		form.save()
		return render(request, 'prontuario/paciente.html', context)


	return render(request, 'prontuario/paciente.html', context)


def paciente_create(request):
	form = PacienteCreateForm(request.POST or None)
	return render(request, 'prontuario/create_paciente.html')

# if request.method == 'POST':
	# 	form = ProfissionalForm(request.POST)
	# 	if form.is_valid():
	# 		prof = Profissional()
	# 		prof.nome = form.cleaned_data['nome']
	# 		prof.sexo = form.cleaned_data['sexo']
	# 		prof.cpf = form.cleaned_data['cpf']
	# 		prof.rg = form.cleaned_data['rg']
	# 		prof.nascimento = form.cleaned_data['nascimento']
	# 		prof.telefone = form.cleaned_data['telefone']
	# 		prof.sus = form.cleaned_data['sus']
	# 		prof.cbo = form.cleaned_data['cbo']
	# 		prof.cnes = form.cleaned_data['cnes']
	# 		prof.cod_equipe = form.cleaned_data['cod_equipe']
	# 		prof.tipo = form.cleaned_data['tipo']
	# 		prof.user.username = form.cleaned_data['username']
	# 		prof.user.password = form.cleaned_data['password']

	# 		prof.save()

	# 		return redirect('login')

	# else:
	# 	form = ProfissionalForm()
	
	# return render(request, 'prontuario/login.html', {'form' : form})