# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cookxplor', '0003_auto_20150829_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languages',
            name='vendor',
        ),
        migrations.AddField(
            model_name='languages',
            name='vendors',
            field=models.ManyToManyField(to='cookxplor.Vendor'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2015, 9, 3, 17, 33, 35, 436696, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='email_id',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='is_available_as_guest_cook',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='picture_path',
            field=models.CharField(null=True, max_length=1500, blank=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='total_experience',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='cusines',
            name='vendor',
        ),
        migrations.AddField(
            model_name='cusines',
            name='vendor',
            field=models.ManyToManyField(to='cookxplor.Vendor'),
        ),
        migrations.RemoveField(
            model_name='locations',
            name='vendor',
        ),
        migrations.AddField(
            model_name='locations',
            name='vendor',
            field=models.ManyToManyField(to='cookxplor.Vendor'),
        ),
        migrations.RemoveField(
            model_name='timings',
            name='vendor',
        ),
        migrations.AddField(
            model_name='timings',
            name='vendor',
            field=models.ManyToManyField(to='cookxplor.Vendor'),
        ),
    ]
