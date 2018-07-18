#!coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Base(models.Model):
    """Model Base para todos os outros models do projeto."""

    class Meta:
        abstract = True

    created = models.DateTimeField('Criado em', default=timezone.now)
    updated = models.DateTimeField('Alterado em', auto_now=True)
