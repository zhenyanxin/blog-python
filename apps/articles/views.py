# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic.base import View
from articles.models import Article
from tags.models import Tag
from django.shortcuts import render


# Create your views here.
class ArticleView(View):
    """标签"""

    def get(self, request):
        """取出博客信息"""
        # print (1/0)
        article = Article.objects.all().get(id=1)
        tags = Tag.objects.all()[:8]
        return render(request, 'blog.html', {
            "article": article,
            "tags": tags,
        })
