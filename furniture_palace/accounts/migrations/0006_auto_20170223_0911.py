# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-23 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170220_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
