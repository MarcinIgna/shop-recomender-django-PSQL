from django.core.management.base import BaseCommand
from shop_recomender.models.order import Order
from shop_recomender.models.user_item_matrix import UserItemMatrix

class Command(BaseCommand):
    help = 'Populates the User-Item Matrix based on order data.'

    def handle(self, *args, **options):
        # Clear existing data in the UserItemMatrix model
        UserItemMatrix.objects.all().delete()

        # Retrieve all orders
        orders = Order.objects.all()

        # Iterate over the orders and populate the UserItemMatrix model
        for order in orders:
            user_item_interaction = UserItemMatrix(
                user=order.user,
                product=order.product,
                interaction=1  # Modify as needed, depending on the type of interaction you want to represent
            )
            user_item_interaction.save()

        self.stdout.write(self.style.SUCCESS('User-Item Matrix successfully populated.'))
