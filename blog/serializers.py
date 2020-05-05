#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]


class PostListSerializer(serializers.Serializer):
    category = CategorySerializer()
    author = UserSerializer()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'created_time',
            'excerpt',
            'category',
            'author',
            'views',
        ]