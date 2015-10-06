# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookxplor', '0007_auto_20150906_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charges',
            name='vendor',
            field=models.ForeignKey(to='cookxplor.Vendor', unique=True),
        ),
    ]
