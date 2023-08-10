from django.urls import path
from shop_recomender.views.user import (
    UserViewCreate, user_redirect, home, shop, add_to_basket,
    checkout, basket_view, thx, logout_view, user_settings, delete_user
    )
from shop_recomender.views.product import ProductView
from shop_recomender.views.admin_view import AdminView
from shop_recomender.views.login import login
from shop_recomender.views.after_login import after_login

app_name = 'user'

urlpatterns = [
    path('', home, name='home'),
    path('reg', UserViewCreate.as_view(), name='regiestration'),
    path('settings/', user_settings, name='user_settings'),
    path('delete_account/', delete_user, name='delete_account'),
    path('redirect/', user_redirect, name='redirection'),
    path("shop/", shop, name="shop" ),
    path('login/', login, name='login'),
    path('home/', after_login, name='main_home'),
    path('home/', after_login, name='admin_home'),
    path("all_users/", AdminView.see_all_users, name="all_users"),
    path("all_products/", AdminView.see_all_products, name="all_products"),
    path("add_product/", ProductView.as_view(), name="add_product"),
    path('add_to_basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('checkout/', checkout, name='checkout'),
    path('basket/', basket_view, name='basket'),
    path('thx/', thx, name='thx'),
    path('logout/', logout_view, name='logout'),
    
    
]