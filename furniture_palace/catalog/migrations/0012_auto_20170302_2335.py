# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20170302_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lenttool',
            name='returned',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='lenttool',
            name='was_damaged',
            field=models.NullBooleanField(),
        ),
    ]
