from django.contrib import admin
from shop_recomender.models.user import User
from shop_recomender.models.product import Product
from shop_recomender.models.order import Order
from shop_recomender.models.review import Review
from shop_recomender.models.category import Category
from shop_recomender.models.user_item_matrix import UserItemMatrix
from shop_recomender.models.adress import Address
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(UserItemMatrix)
admin.site.register(Address)

