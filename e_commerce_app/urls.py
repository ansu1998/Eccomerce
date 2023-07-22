# e_commerce_app/urls.py

from django.urls import path
from .views import CustomerListCreateView, CustomerRetrieveUpdateDestroyView, ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-retrieve-update-destroy'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]
