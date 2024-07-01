
from django.urls import path
from .views import get_all_ads, search_ads, create_ad, get_ad, create_proposal, delete_proposal


urlpatterns = [
    path('ads/', create_ad, name='create_ad'),  # 게시글 작성
    path('ads/<int:pk>/', get_ad, name='get_ad'),  # 특정 게시물 조회
    path('ads/<int:ad_id>/proposals/', create_proposal, name='create_proposal'),  # 댓글 작성
    path('ads/<int:ad_id>/proposals/<int:pk>/delete/', delete_proposal, name='delete_proposal'),  # 댓글 삭제
    path('', get_all_ads, name='get_all_ads'),  # 초기 화면 설정
    path('ads/search/', search_ads, name='search_ads'),  # 제목 검색
]
