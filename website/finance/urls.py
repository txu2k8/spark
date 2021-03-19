#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : urls.py
@Time  : 2020/12/10 9:41
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

from django.urls import path
# from django.conf.urls import url
from . import views


app_name = 'finance'

urlpatterns = [
    # index page
    path(r'', views.IndexView.as_view(), name='index'),
    path('bank_screws/', views.BankScrewsView.as_view(), name='bank_screws'),
    path('bank_screws/index_valuation', views.BankScrewsIndexValuationView.as_view(), name='bank_screws_index_valuation'),
]


if __name__ == '__main__':
    pass
