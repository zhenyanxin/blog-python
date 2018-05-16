# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic.base import View
from articles.models import Article
from archives.models import Archive
from django.shortcuts import render


# Create your views here.
class ArchivesView(View):
    """归档"""

    def get(self, request):
        """取出博客信息"""
        # print (1/0)
        article = Article.objects.all()
        archives=Archive.objects.all()
        return render(request, 'archives.html', {
            "article": article,
            "archives": archives,
        })
