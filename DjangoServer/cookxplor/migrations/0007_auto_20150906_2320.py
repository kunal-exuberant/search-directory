# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookxplor', '0006_auto_20150905_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timings',
            name='end_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='timings',
            name='start_time',
            field=models.IntegerField(),
        ),
    ]
