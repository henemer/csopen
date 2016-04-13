# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160219_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'fornecedor', 'verbose_name_plural': 'fornecedores'},
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='observation',
        ),
        migrations.AddField(
            model_name='supplier',
            name='obsevations',
            field=models.TextField(blank=True, verbose_name='observações'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, verbose_name='cnpj'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='code',
            field=models.IntegerField(unique=True, verbose_name='código'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='company',
            field=models.CharField(max_length=100, verbose_name='razão social'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='trade',
            field=models.CharField(blank=True, max_length=100, verbose_name='nome fantasia'),
        ),
    ]