# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"名称")

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
