#!/usr/bin/env python
# encoding: utf-8
import xadmin
from .models import Article


class ArticleAdmin(object):
    list_display = ['title', 'type', 'add_time', 'publisher']


xadmin.site.register(Article, ArticleAdmin)
