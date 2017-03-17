# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prontuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 5, 18, 19, 18, 959839), blank=True),
        ),
    ]
