# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]
