from django.contrib import admin
from django.urls import path

from .views import create_ad

urlpatterns = [
    # 광고 게시물 생성
    path('ads/', create_ad, name='create_ad')
]