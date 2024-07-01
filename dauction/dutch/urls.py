from django.urls import re_path

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi
from django.urls import path
from .views import get_all_ads, search_ads, create_ad, get_ad, create_proposal, delete_proposal

schema_view = get_schema_view(
    openapi.Info(
        title="프로젝트 이름(예: likelion-project)",
        default_version='프로젝트 버전(예: 1.1.1)',
        description="해당 문서 설명(예: likelion-project API 문서)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="likelion@inha.edu"), # 부가정보
        license=openapi.License(name="backend"),     # 부가정보
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
     # Swagger url
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('ads/', create_ad, name='create_ad'),  # 게시글 작성
    path('ads/<int:pk>/', get_ad, name='get_ad'),  # 특정 게시물 조회
    path('ads/<int:ad_id>/proposals/', create_proposal, name='create_proposal'),  # 댓글 작성
    path('ads/<int:ad_id>/proposals/<int:pk>/delete/', delete_proposal, name='delete_proposal'),  # 댓글 삭제
    path('', get_all_ads, name='get_all_ads'),  # 초기 화면 설정
    path('ads/search/', search_ads, name='search_ads'),  # 제목 검색
]