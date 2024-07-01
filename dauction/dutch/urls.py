from django.urls import path
from .views import create_ad, get_ad, create_proposal, delete_proposal

urlpatterns = [
    path('ads/', create_ad, name='create_ad'),
    path('ads/<int:ad_id>/', create_proposal, name='create_proposal'),
    path('postad/<int:ad_id>/<int:pk>/delete/', delete_proposal, name='delete_proposal'),
    path('postad/<int:pk>/', get_ad, name='get_ad'),
]
