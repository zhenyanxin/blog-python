# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from articles.models import Article


# Create your models here.
class Archive(models.Model):
    time = models.CharField(max_length=100, verbose_name=u"时间")
    article = models.ForeignKey(Article, verbose_name=u"文章")

    class Meta:
        verbose_name = u"归档"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.time
