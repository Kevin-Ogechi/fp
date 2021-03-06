# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-20 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170220_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='furniture_category',
            field=models.CharField(choices=[('Beds', 'Beds'), ('Seats', 'Seats'), ('Tables', 'Tables')], default='Choose', max_length=200),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='furniture_name',
            field=models.CharField(choices=[('Double', 'Double Bed'), ('Single', 'Single Bed'), ('Double Decker', 'Double Decker'), ('Coffee Table', 'Coffee Table'), ('Dinning Table', 'Dinning Table'), ('Kitchen Table', 'Kitchen Table'), ('Office Table', 'Office Table'), ('Arm Chair', 'Arm Chair'), ('Classroom Chairs', 'Classroom Chair'), ('Office Chairs', 'Office Chair'), ('Benches', 'Benches')], default='Choose', max_length=50),
        ),
    ]
