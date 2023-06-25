from django.urls import path
from shop_recomender.views.user import UserViewCreate, user_redirect, home
from shop_recomender.views.product import ProductView
from shop_recomender.views.admin_view import AdminView
from shop_recomender.views.login import login
from shop_recomender.views.after_login import after_login

app_name = 'user'

urlpatterns = [
    path('', home, name='home'),
    path('reg', UserViewCreate.as_view(), name='regiestration'),
    path('redirect/', user_redirect, name='redirection'),
    path('login/', login, name='login'),
    path('home/', after_login, name='main_home'),
    path('home/', after_login, name='admin_home'),
    path("all_users/", AdminView.see_all_users, name="all_users"),
    path("all_products/", AdminView.see_all_products, name="all_products"),
    path("add_product/", ProductView.as_view(), name="add_product"),
    
]