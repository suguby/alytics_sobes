# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 16:43
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_in', django.contrib.postgres.fields.jsonb.JSONField(default='[]', verbose_name='Входной набор')),
                ('data_out', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Результат последней проверки')),
                ('exceptions', models.TextField(default='', verbose_name='Исключения в ходе последней проверке')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено')),
            ],
        ),
    ]