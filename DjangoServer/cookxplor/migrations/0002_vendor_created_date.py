# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cookxplor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 8, 28, 22, 4, 52, 37569, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
