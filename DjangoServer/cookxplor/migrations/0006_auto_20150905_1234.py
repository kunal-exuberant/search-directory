# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookxplor', '0005_auto_20150903_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cusines',
            name='vendors',
        ),
        migrations.RemoveField(
            model_name='languages',
            name='vendors',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='vendors',
        ),
        migrations.RemoveField(
            model_name='timings',
            name='vendors',
        ),
        migrations.AddField(
            model_name='vendor',
            name='cusines',
            field=models.ManyToManyField(to='cookxplor.Cusines'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='languages',
            field=models.ManyToManyField(to='cookxplor.Languages'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='locations',
            field=models.ManyToManyField(to='cookxplor.Locations'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='timings',
            field=models.ManyToManyField(to='cookxplor.Timings'),
        ),
    ]
