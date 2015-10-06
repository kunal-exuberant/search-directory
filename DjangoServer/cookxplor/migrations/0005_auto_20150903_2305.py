# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookxplor', '0004_auto_20150903_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cusines',
            old_name='vendor',
            new_name='vendors',
        ),
        migrations.RenameField(
            model_name='locations',
            old_name='vendor',
            new_name='vendors',
        ),
        migrations.RenameField(
            model_name='timings',
            old_name='vendor',
            new_name='vendors',
        ),
    ]
