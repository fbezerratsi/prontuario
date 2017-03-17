# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prontuario', '0003_auto_20170306_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 3, 6, 23, 38, 35, 127011), blank=True),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2017, 3, 6, 23, 38, 35, 127054), blank=True),
        ),
        migrations.RemoveField(
            model_name='consultas',
            name='paciente',
        ),
        migrations.AddField(
            model_name='consultas',
            name='paciente',
            field=models.ForeignKey(default=1, to='prontuario.Paciente'),
            preserve_default=False,
        ),
    ]
