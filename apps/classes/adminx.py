#!/usr/bin/env python
# encoding: utf-8
import xadmin
from .models import Type


class TypeAdmin(object):
    list_display = ['name']


xadmin.site.register(Type, TypeAdmin)
