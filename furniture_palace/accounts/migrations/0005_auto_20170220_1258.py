# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-20 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170216_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_physical_address',
            field=models.TextField(default='a physical address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_address',
            field=models.CharField(max_length=255),
        ),
    ]
