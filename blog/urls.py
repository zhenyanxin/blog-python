# -*- coding: utf-8 -*-
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import xadmin
from django.conf.urls import url
from users.views import IndexView, AboutView, BlogInputView, BlogsView, page_not_found, page_error
from articles.views import ArticleView
from tags.views import TagView
from classes.views import TypeView
from archives.views import ArchivesView
from settings import MEDIA_ROOT
from django.views.static import serve

# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/', IndexView.as_view(), name="index"),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r"^tags/", TagView.as_view(), name="tags"),
    url(r"^types", TypeView.as_view(), name="types"),
    url(r"^archives", ArchivesView.as_view(), name="archives"),
    url(r"^about", AboutView.as_view(), name="about"),
    url(r'^blog/', ArticleView.as_view(), name="blog"),
    url(r"^issue", BlogInputView.as_view(), name="issue"),
    url(r"^admin", BlogsView.as_view(), name="admin"),

    # 配置上传函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
# 全局404页面配置
handler404 = page_not_found
handler500 = page_error
