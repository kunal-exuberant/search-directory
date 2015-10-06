# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookxplor', '0002_vendor_created_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cusine',
            new_name='Cusines',
        ),
        migrations.RenameModel(
            old_name='Location',
            new_name='Locations',
        ),
    ]
