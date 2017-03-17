# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prontuario', '0005_auto_20170306_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 3, 12, 13, 23, 9, 756430), blank=True),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2017, 3, 12, 13, 23, 9, 756472), blank=True),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='profissionais',
            field=models.ManyToManyField(to='prontuario.Profissional', blank=True),
        ),
    ]
