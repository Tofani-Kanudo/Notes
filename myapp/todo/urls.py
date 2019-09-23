# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:52:42 2019

@author: Yashesh
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]