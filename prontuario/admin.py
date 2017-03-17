from django.contrib import admin
from prontuario.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
admin.autodiscover()


class PacienteAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome', 'nascimento', 'sus', 'get_familia', 'situacao', 'responsavel')
	search_fields = ('nome', 'nascimento', 'sus', 'situacao')

class ProfissionalAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome', 'nascimento', 'user', 'tipo')
	search_fields = ('nome', 'nascimento', 'user', 'tipo')

class EnderecoAdmin(admin.ModelAdmin):
	list_display = ('rua', 'numero', 'bairro', 'cep', 'cidade', 'estado')
	search_fields = ('rua', 'numero', 'bairro', 'cep', 'cidade', 'estado')

class MicroAreaAdmin(admin.ModelAdmin):
	list_display = ('nome_area', 'numero', 'profissional')
	search_fields = ('nome_area', 'numero', 'profissional')

class FamiliaAdmin(admin.ModelAdmin):
	list_display = ['num_prontuario', 'endereco', 'micro_area']
	search_fields = ['num_prontuario']

class TipoProfissionalAdmin(admin.ModelAdmin):
	list_display = ['id', 'nome']
	search_fields = ['nome']

class ConsultasAdmin(admin.ModelAdmin):
	list_display = ('id', 'data', 'hora', 'get_profissionais', 'get_paciente')
	search_fields = ('data', 'get_profissionais', 'get_paciente')

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(MicroArea, MicroAreaAdmin)
admin.site.register(Familia, FamiliaAdmin)
admin.site.register(TipoProfissional, TipoProfissionalAdmin)
admin.site.register(Consultas, ConsultasAdmin)
