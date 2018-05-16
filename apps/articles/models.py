# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField
from users.models import UserProfile
from tags.models import Tag
from classes.models import Type


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name=u"标题")
    guide = models.TextField(max_length=300, default=u"", verbose_name=u"引用")
    origin = models.CharField(max_length=100, choices=(("原创", "原创"), ("引用", "引用"), ("转载", "转载")), default=u"原创",
                              verbose_name=u"来源")
    content = UEditorField(imagePath="article/images/", width=1000, height=300,
                           filePath="article/files/", default='', verbose_name=u"内容")
    tag = models.ManyToManyField(Tag, verbose_name=u"标签")
    type = models.ForeignKey(Type, verbose_name=u"分类")
    image = models.ImageField(upload_to="article/images", default="article/images/default.jpg", verbose_name=u"图片")
    publisher = models.ForeignKey(UserProfile, verbose_name=u"发布者")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"发布时间")

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
