# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lenttool',
            name='temp_carpenter',
        ),
        migrations.RemoveField(
            model_name='lenttool',
            name='tool',
        ),
        migrations.DeleteModel(
            name='LentTool',
        ),
    ]