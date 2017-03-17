# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prontuario', '0002_auto_20170305_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultas',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2017, 3, 6, 22, 3, 46, 731142), blank=True),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='data',
            field=models.DateField(default=datetime.datetime(2017, 3, 6, 22, 3, 46, 731099), blank=True),
        ),
    ]
