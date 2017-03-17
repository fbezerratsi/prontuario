# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(default=datetime.datetime(2017, 3, 5, 18, 17, 37, 155476), blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(default=b's/n', max_length=50, null=True, blank=True)),
                ('bairro', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=2, verbose_name='Sexo', choices=[(b'AC', b'Acre'), (b'AL', b'Alagoas'), (b'AP', b'Amap\xc3\xa1'), (b'BA', b'Bahia'), (b'CE', b'Cear\xc3\xa1'), (b'DF', b'Distrito Federal'), (b'ES', b'Esp\xc3\xadrito Santo'), (b'GO', b'Goi\xc3\xa1s'), (b'MA', b'Maran\xc3\xa3o'), (b'MG', b'Minas Gerais'), (b'MS', b'Mato Grosso do Sul'), (b'MT', b'Mato Grosso'), (b'PA', b'Par\xc3\xa1'), (b'PB', b'Para\xc3\xadba'), (b'PE', b'Pernanbuco'), (b'PI', b'Piau\xc3\xad'), (b'PR', b'Paran\xc3\xa1'), (b'RJ', b'Rio de Janeiro'), (b'RN', b'Rio Grande do Norte'), (b'RO', b'Rond\xc3\xb4nia'), (b'RR', b'Roraima'), (b'RS', b'Rio Grande do Sul'), (b'SC', b'Santa Catarina'), (b'SE', b'Sergipe'), (b'SP', b'S\xc3\xa3o Paulo'), (b'TO', b'Tocantins')])),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_prontuario', models.IntegerField(default=0, null=True, blank=True)),
                ('endereco', models.OneToOneField(to='prontuario.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='MicroArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_area', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('cpf', models.CharField(max_length=200, null=True, blank=True)),
                ('rg', models.CharField(max_length=100, null=True, blank=True)),
                ('telefone', models.CharField(max_length=20, null=True, blank=True)),
                ('nascimento', models.DateField()),
                ('sus', models.CharField(max_length=255, null=True, blank=True)),
                ('responsavel', models.BooleanField(default=1)),
                ('situacao', models.CharField(max_length=19, verbose_name='Situa\xe7\xe3o', choices=[(b'ATIVO', b'Paciente na \xc3\x81rea'), (b'FORA DE AREA', b'Paciente Fora de \xc3\x81rea'), (b'FALECIDO', b'Paciente Falecido')])),
                ('familia', models.ForeignKey(to='prontuario.Familia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('cpf', models.CharField(max_length=200, null=True, blank=True)),
                ('rg', models.CharField(max_length=100, null=True, blank=True)),
                ('telefone', models.CharField(max_length=20, null=True, blank=True)),
                ('nascimento', models.DateField()),
                ('sus', models.CharField(max_length=16, null=True, blank=True)),
                ('cbo', models.CharField(max_length=16, null=True, blank=True)),
                ('cnes', models.CharField(max_length=16, null=True, blank=True)),
                ('cod_equipe', models.CharField(max_length=16, null=True, blank=True)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='TipoProfissional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='profissional',
            name='tipo',
            field=models.ForeignKey(to='prontuario.TipoProfissional'),
        ),
        migrations.AddField(
            model_name='profissional',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='microarea',
            name='profissional',
            field=models.OneToOneField(to='prontuario.Profissional'),
        ),
        migrations.AddField(
            model_name='familia',
            name='micro_area',
            field=models.ForeignKey(to='prontuario.MicroArea'),
        ),
        migrations.AddField(
            model_name='consultas',
            name='paciente',
            field=models.ManyToManyField(to='prontuario.Paciente'),
        ),
        migrations.AddField(
            model_name='consultas',
            name='profissionais',
            field=models.ManyToManyField(to='prontuario.Profissional'),
        ),
    ]
