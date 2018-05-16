#!/usr/bin/env python
# encoding: utf-8
import xadmin
from .models import Archive


class ArchiveAdmin(object):
    list_display = ['time','article']


xadmin.site.register(Archive, ArchiveAdmin)
