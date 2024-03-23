# 함수 기반 뷰로 로그인 구현하기
# accounts > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('logincheck/', views.logincheck, name='logincheck'),
    path('loginfbv/', views.loginfbv, name='loginfbv'),
]