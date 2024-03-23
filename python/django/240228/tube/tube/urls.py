from django.urls import path
from .views import TubeListView, TubeDetailView, TubeCreateView, TubeUpdateView, TubeDeleteView, TubeTagListView

urlpatterns = [
    path("", TubeListView.as_view(), name="tube_list"),
    path("<int:pk>/", TubeDetailView.as_view(), name="tube_detail"),
    path("create/", TubeCreateView.as_view(), name="tube_create"),
    path("<int:pk>/update/", TubeUpdateView.as_view(), name="tube_update"),
    path("<int:pk>/delete/", TubeDeleteView.as_view(), name="tube_delete"),
    path("tag/<str:tag>/", TubeTagListView.as_view(), name="tube_tag"),
]
