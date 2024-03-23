from django.urls import path
from . import views # 현재폴더에 있는 views.py

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
# name이 있는 이유는 이 URL의 고유 별칭이다.
# 템플릿같은 곳에서 이 별칭을 이용해 이 URL에 접근할 수 있다.