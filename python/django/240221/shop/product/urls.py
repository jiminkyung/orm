from django.urls import path
from .views import product, product_details

urlpatterns = [
    path("", product),
    path("<int:pk>/", product_details),
]