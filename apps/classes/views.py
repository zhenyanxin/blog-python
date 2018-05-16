# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic.base import View
from articles.models import Article
from classes.models import Type
from django.shortcuts import render


# Create your views here.
class TypeView(View):
    """分类"""

    def get(self, request):
        """取出博客信息"""
        # print (1/0)
        article_list = Article.objects.all()
        recommend = Article.objects.all()[:10]
        types = Type.objects.all()[:8]
        paginator = Paginator(article_list, 5)
        page = request.GET.get('page')
        try:
            article = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            article = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            article = paginator.page(paginator.num_pages)
        return render(request, 'types.html', {
            "article": article,
            "types": types,
            "recommends": recommend,
        })
