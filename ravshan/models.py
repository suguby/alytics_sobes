# -*- coding: utf-8 -*-
from django.contrib.postgres.fields import JSONField
from django.db import models


class DataSet(models.Model):
    data_in = JSONField(verbose_name='Входной набор', default='[]')
    data_out = JSONField(verbose_name='Результат последней проверки', null=True, blank=True)
    exceptions = models.TextField(verbose_name='Исключения в ходе последней проверке', default='')
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True, null=True)
    modified_at = models.DateTimeField(verbose_name='Изменено', auto_now=True, null=True)

