from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("posts/", include("posts.urls")),
    path(
        "admin/", admin.site.urls
    ),  # admin 페이지(일반적인 drf에서 사용하진 않습니다.)
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # 스키마
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),  # 스웨거
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),  # 문서화
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
