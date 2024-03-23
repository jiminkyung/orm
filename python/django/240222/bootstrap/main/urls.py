from django.urls import path
from . import views # 현재폴더에 있는 views.py

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]