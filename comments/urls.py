#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang

from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]