# e_commerce_app/views.py

from rest_framework import generics
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer
from datetime import datetime, timedelta

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        # Check if the product was registered more than 2 months ago
        product = serializer.instance
        two_months_ago = datetime.now() - timedelta(days=60)

        if product.created_at <= two_months_ago:
            is_active = self.request.data.get('is_active', None)

            # Only set is_active to False if it's not already False
            if is_active is False and product.is_active:
                serializer.save(is_active=False)
            else:
                serializer.save()
        else:
            # If the product was registered less than 2 months ago, keep it active
            serializer.save()

# E:\Eccomerce\e_commerce_project\e_commerce_app