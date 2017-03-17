from django.forms import ModelForm, forms
from prontuario.models import *
from  django import forms


class EnderecoForm(ModelForm):
	def __init__(self, * args, **kwargs):
		super(EnderecoForm, self).__init__(*args, **kwargs)

		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

	class Meta():
		model = Endereco
		fields = ['rua', 'numero', 'bairro', 'cep', 'cidade', 'estado']

class ConsultaForm(ModelForm):
	def __init__(self, * args, **kwargs):
		super(ConsultaForm, self).__init__(*args, **kwargs)

		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

		self.fields['data'].widget.attrs.update({
			'type': 'date',
		})
		self.fields['paciente'].widget.attrs.update({
			'class': 'selectpicker',
			'data-live-search': 'true',
			#'required': 'true',
		})
		self.fields['profissionais'].widget.attrs.update({
			'class': 'selectpicker',
			'data-live-search': 'true',
			'required': 'true',
		})

	class Meta():
		model = Consultas
		fields = ['data', 'profissionais', 'paciente']

class TipoProfissionalForm(ModelForm):
	def __init__(self, * args, **kwargs):
		super(TipoProfissionalForm, self).__init__(*args, **kwargs)

		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})

	class Meta():
		model = TipoProfissional
		fields = ['nome']


class PacienteForm(ModelForm):
	#familia = forms.ModelChoiceField(queryset=Familia.objects.all())
	def __init__(self, * args, **kwargs):
		super(PacienteForm, self).__init__(*args, **kwargs)

		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control',
			})
		self.fields['cpf'].widget.attrs.update({
				'id': 'cpf',
			})
		self.fields['telefone'].widget.attrs.update({
			'id': 'telefone',
		})
		self.fields['nascimento'].widget.attrs.update({
			'id': 'data_nascimento',
		})

	class Meta():
		model = Paciente
		fields = ['situacao', 'nome', 'sexo', 'cpf', 'rg', 'telefone', 'nascimento', 'sus', 'responsavel', 'familia']


			

# class ProfissionalForm(forms.ModelForm):
# 	class Meta():
# 		model = Profissional
# 		fields = ['nome', 'sexo', 'cpf', 'rg', 'nascimento', 'telefone', 'sus', 'cbo', 'cnes', 'cod_equipe', 'tipo']


# class UserForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'first_name', 'last_name', 'password']



# class PacienteCreateForm(forms.ModelForm):
# 	familia = forms.ModelChoiceField(queryset=Familia.objects.all().order_by('id'), widget=forms.Select)
# 	class Meta:
# 		model = Paciente
# 		fields = ['familia','responsavel']
	# class Meta:
	# 	model = Paciente