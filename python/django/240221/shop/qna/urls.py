from django.urls import path
from .views import qna, qna_details

urlpatterns = [
    path('', qna),
    path('<int:pk>/', qna_details),
]