# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from django.views.generic.base import View
from articles.models import Article
from tags.models import Tag
from classes.models import Type


# Create your views here.
class IndexView(View):
    """首页"""

    def get(self, request):
        """取出博客信息"""
        # print (1/0)
        article_list = Article.objects.all()
        recommend = Article.objects.all()[:10]
        tags = Tag.objects.all()[:8]
        types = Type.objects.all()[:15]
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
        return render(request, 'index.html', {
            "article": article,
            "article_list": article_list,
            "tags": tags,
            "types": types,
            "recommends": recommend,
        })


def page_not_found(request):
    # 全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    # 全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response


class AboutView(View):
    """首页"""

    def get(self, request):
        """取出博客信息"""
        return render(request, 'about.html')


class BlogsView(View):
    """博客后台"""

    def get(self, request):
        """取出博客信息"""
        return render(request, 'admin/blogs.html')


class BlogInputView(View):
    """博客发布"""

    def get(self, request):
        """取出博客信息"""
        return render(request, 'admin/blog-input.html')
