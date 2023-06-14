from django.db import models
from shop_recomender.models.user import User
from shop_recomender.models.product import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
