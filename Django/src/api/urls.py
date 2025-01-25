from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/api/products
    path('products/', views.get_all_products),
]
