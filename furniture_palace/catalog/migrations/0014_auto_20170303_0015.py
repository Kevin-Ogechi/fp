# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-03 00:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_lenttool_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lenttool',
            old_name='days',
            new_name='days_with_tool',
        ),
    ]