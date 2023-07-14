from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop_recomender.models.user import User
from shop_recomender.models.product import Product
from shop_recomender.models.user_item_matrix import UserItemMatrix

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

@receiver(post_save, sender=Order)
def update_user_item_matrix(sender, instance, created, **kwargs):
    if created:
        # Create or update the UserItemMatrix based on the new order
        user_item_interaction, _ = UserItemMatrix.objects.update_or_create(
            user=instance.user,
            product=instance.product,
            defaults={'interaction': 1}  # Modify as needed
        )
        # You can perform additional logic here based on your requirements
