# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookxplor', '0008_auto_20150907_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charges',
            name='vendor',
            field=models.OneToOneField(to='cookxplor.Vendor'),
        ),
    ]
