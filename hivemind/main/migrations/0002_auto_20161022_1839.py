# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='name',
            field=models.CharField(max_length=2000),
        ),
    ]