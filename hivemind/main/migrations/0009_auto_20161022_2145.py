# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_entity_in_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='in_session',
        ),
        migrations.AlterField(
            model_name='entity',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]