from django.urls import path
from .views import create_ad, create_proposal

urlpatterns = [
    path('ads/', create_ad, name='create_ad'),
    path('ads/<int:ad_id>/', create_proposal, name='create_proposal'),
]
