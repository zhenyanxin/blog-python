#!/usr/bin/env python
# encoding: utf-8
import xadmin
from .models import Tag


class TagAdmin(object):
    list_display = ['name']


xadmin.site.register(Tag, TagAdmin)
