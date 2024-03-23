from django.urls import path
from .views import notice, free, free_details, onenone, onenone_details

urlpatterns = [
    path("", notice),
    path("free/", free),
    path("free/<int:pk>/", free_details),
    path("onenone/", onenone),
    path("onenone/<int:pk>/", onenone_details),
]