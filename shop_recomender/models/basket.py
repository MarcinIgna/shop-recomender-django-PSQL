from django.db import models
from shop_recomender.models.product import Product
from shop_recomender.models.user import User

class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_product(self, product):
        self.products.add(product)

    def remove_product(self, product):
        self.products.remove(product)

    def clear(self):
        self.products.clear()

    def calculate_total_price(self):
        total_price = sum(product.price for product in self.products.all())
        return total_price