#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""为应用程序的users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 登录界面
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
]