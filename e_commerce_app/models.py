from django.db import models
from django.utils import timezone

# Create your models here.
# e_commerce_app/models.py

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    seller = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
