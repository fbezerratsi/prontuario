# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prontuario', '0004_auto_20170306_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 3, 6, 23, 40, 47, 471106), blank=True),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2017, 3, 6, 23, 40, 47, 471149), blank=True),
        ),
        migrations.RemoveField(
            model_name='consultas',
            name='paciente',
        ),
        migrations.AddField(
            model_name='consultas',
            name='paciente',
            field=models.ManyToManyField(to='prontuario.Paciente'),
        ),
    ]
