#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.brucecode.xyz', '114.116.232.108']