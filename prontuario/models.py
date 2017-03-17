#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import time

class Pessoa(models.Model):
	CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
	nome = models.CharField(max_length=255)
	sexo = models.CharField(u'Sexo', max_length=1, choices=CHOICES_SEXO)
	cpf = models.CharField(max_length=200, blank=True, null= True)
	rg = models.CharField(max_length=100, blank=True, null= True)
	telefone = models.CharField(max_length=20, blank=True, null= True)
	nascimento = models.DateField()

	class Meta:
		abstract = True

class TipoProfissional(models.Model):
	nome = models.CharField(max_length=60)

	def __unicode__(self):
		return self.nome	

class Profissional(Pessoa):
	#CHOICES_PROFISSIONAL = (('Med', 'Medico'), ('Enf', 'Enfermeiro'), ('Psi', 'Psicologo'), ('Den', 'Dentista'))
 	user = models.OneToOneField(User, unique=True)
 	sus = models.CharField(max_length=16, blank=True, null= True)
 	cbo = models.CharField(max_length=16, blank=True, null= True)
 	cnes = models.CharField(max_length=16, blank=True, null= True)
 	cod_equipe = models.CharField(max_length=16, blank=True, null= True)
 	tipo = models.ForeignKey("TipoProfissional")

 	def __unicode__(self):
 		return self.nome

 	class Meta:
 		#ordenar pelo nome
 		ordering = ['nome']


class Consultas(models.Model):
	data = models.DateField(default=datetime.now(), blank=True)
	hora = models.TimeField(default=datetime.now(), blank=True)
	profissionais = models.ManyToManyField("Profissional", blank=True)
	paciente = models.ManyToManyField("Paciente")
	
	def __unicode__(self):
		return "data"

	def get_profissionais(self):
		return " | ".join([str(p) for p in self.profissionais.all()])

	def get_paciente(self):
		return " | ".join([str(p) for p in self.paciente.all()])

	def procurar_paciente(self, paciente):
		pass


class MicroArea(models.Model):
 	nome_area = models.CharField(max_length=255)
 	numero = models.CharField(max_length=255)
 	profissional = models.OneToOneField("Profissional")

 	def __unicode__(self):
 		return self.nome_area

class Endereco(models.Model):
	rua = models.CharField(max_length=255)
	#numero = models.IntegerField(default=0, blank=True, null= True)
	numero = models.CharField(max_length=50, default='s/n', blank=True, null=True)
	bairro = models.CharField(max_length=255)
	cep = models.CharField(max_length=50)
	cidade = models.CharField(max_length=200)

	UF_CHOICES = (
	    ('AC', 'Acre'), 
	    ('AL', 'Alagoas'),
	    ('AP', 'Amapá'),
	    ('BA', 'Bahia'),
	    ('CE', 'Ceará'),
	    ('DF', 'Distrito Federal'),
	    ('ES', 'Espírito Santo'),
	    ('GO', 'Goiás'),
	    ('MA', 'Maranão'),
	    ('MG', 'Minas Gerais'),
	    ('MS', 'Mato Grosso do Sul'),
	    ('MT', 'Mato Grosso'),
	    ('PA', 'Pará'),
	    ('PB', 'Paraíba'),
	    ('PE', 'Pernanbuco'),
	    ('PI', 'Piauí'),
	    ('PR', 'Paraná'),
	    ('RJ', 'Rio de Janeiro'),
	    ('RN', 'Rio Grande do Norte'),
	    ('RO', 'Rondônia'),
	    ('RR', 'Roraima'),
	    ('RS', 'Rio Grande do Sul'),
	    ('SC', 'Santa Catarina'),
	    ('SE', 'Sergipe'),
	    ('SP', 'São Paulo'),
	    ('TO', 'Tocantins')
	)
	estado = models.CharField(u'Sexo', max_length=2, choices=UF_CHOICES)

	def __unicode__(self):
 		return self.rua


class Familia(models.Model):
	num_prontuario = models.IntegerField(default=0, blank=True, null= True)
	endereco = models.OneToOneField("Endereco")
	micro_area = models.ForeignKey("MicroArea")

	# def get_micro_area(self):
	# 	return ", ".join([str(p) for p in self.micro_area.all()])

	def __unicode__(self):
 		return str(self.num_prontuario) + " - " + self.endereco.rua	+ ", N: " + self.endereco.numero

class Paciente(Pessoa):
	sus = models.CharField(max_length=255, blank=True, null= True)
	responsavel = models.BooleanField(default=1)
	familia = models.ForeignKey("Familia")
	CHOICES_SITUACAO = (
		('ATIVO', 'Paciente na Área'), 
		('FORA DE AREA', 'Paciente Fora de Área'),
		('FALECIDO', 'Paciente Falecido'),
	)
	situacao = models.CharField(u'Situação', max_length=19, choices=CHOICES_SITUACAO)

	def is_responsavel(self):
		return bool(self.responsavel)

	def get_familia(self):
		return self.familia.num_prontuario

	def __unicode__(self):
 		return self.nome

#class AgenteSaude(Profissional):
	#profissional = models.OneToOneField("Profissional")
	#micro_area = models.OneToOneField("MicroArea")




# class Endereco(models.Model):
# 	Pessoa = models.ForeignKey(Pessoa)
# 	rua = models.CharField(max_length=255)
# 	numero = models.CharField(max_length=255)
# 	bairro = models.CharField(max_length=255)
# 	cep = models.CharField(max_length=50)
# 	cidade = models.CharField(max_length=200)
# 	estado = models.CharField(max_length=200)

# class Familia(models.Model):
# 	paciente = models.ForeignKey(Paciente, verbose_name=u'Paciente')
# 	endereco = models.ForeignKey(Endereco)
# 	micro_area = models.ForeignKey(MicroArea)

# class Profissional(models.Model):
# 	user = models.OneToOneField(User)