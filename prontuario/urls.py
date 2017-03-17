from django.conf.urls import url
from prontuario import views

urlpatterns = [
	url(r'^$', views.nada, name="nada"),
    url(r'^home/$', views.home, name="home"),
    url(r'^login/$', views.do_login, name="login"),
    url(r'^logout/$', views.do_logout, name="logout"),

    url(r'^consulta/$', views.consulta, name="consulta"),
    url(r'^consulta/create/$', views.consulta_create, name="consulta_create"),
    url(r'^consulta/abrir/$', views.abrir_consulta, name="abrir_consulta"),
    url(r'^consulta/update/$', views.consulta_update, name="consulta_update"),
    url(r'^consulta_do_dia/$', views.consulta_do_dia, name="consulta_do_dia"),
    url(r'^filtrar_consulta/$', views.filtrar_consulta, name="filtrar_consulta"),

    url(r'^paciente/(?P<id_paciente>\d+)/$', views.visualizar_paciente, name="visualizar_paciente"),
    url(r'^tabela/$', views.tabela, name="tabela"),
    url(r'^endereco/create/$', views.endereco_create, name="endereco_create"),
    url(r'^paciente/create/$', views.paciente_create, name="paciente_create"),
]