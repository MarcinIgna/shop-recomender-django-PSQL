from django.db import models
from shop_recomender.models.category import Category

class Product(models.Model):
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)