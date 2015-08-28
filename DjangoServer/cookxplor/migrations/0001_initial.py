# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('min_charge', models.DecimalField(max_digits=6, decimal_places=2)),
                ('min_charge_People', models.IntegerField()),
                ('max_People', models.IntegerField()),
                ('average_charge_per_Person', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
            options={
                'db_table': 'charges',
            },
        ),
        migrations.CreateModel(
            name='Cusine',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cuisine_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cuisine',
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100)),
                ('state_name', models.CharField(max_length=100)),
                ('pincode', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Timings',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
            ],
            options={
                'db_table': 'timings',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(null=True, blank=True, max_length=100)),
                ('contact_no', models.CharField(max_length=100)),
                ('foodtype', models.CharField(max_length=10, choices=[(1, 'Veg'), (2, 'Non-Veg'), (3, 'Both')], default=3)),
                ('verification', models.BooleanField()),
                ('chargespermonth', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
        migrations.AddField(
            model_name='timings',
            name='vendor',
            field=models.ForeignKey(to='cookxplor.Vendor'),
        ),
        migrations.AddField(
            model_name='location',
            name='vendor',
            field=models.ForeignKey(to='cookxplor.Vendor'),
        ),
        migrations.AddField(
            model_name='languages',
            name='vendor',
            field=models.ForeignKey(to='cookxplor.Vendor'),
        ),
        migrations.AddField(
            model_name='cusine',
            name='vendor',
            field=models.ForeignKey(to='cookxplor.Vendor'),
        ),
        migrations.AddField(
            model_name='charges',
            name='vendor',
            field=models.ForeignKey(to='cookxplor.Vendor'),
        ),
    ]
