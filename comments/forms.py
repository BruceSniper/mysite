#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
