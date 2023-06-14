from django.urls import path
from shop_recomender.views.user import UserView
from shop_recomender.views.home import HomeView
from shop_recomender.views.product import ProductView
from shop_recomender.views.admin_view import AdminView

app_name = 'shop_recomender'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_user/', UserView.add_user, name='add_user'),
    path("all_products/", ProductView.get_all_products, name="all_products"),
    path("get_product/<int:product_id>/", ProductView.get_product, name="get_product"),
    path('delete_user/<int:user_id>/', UserView.delete_user, name='delete_user'),
    path("admin_viev/all_users/", AdminView.see_all_users, name="all_users"),
]