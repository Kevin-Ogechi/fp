# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20170302_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpayment',
            name='days_in_store',
            field=models.IntegerField(null=True),
        ),
    ]
