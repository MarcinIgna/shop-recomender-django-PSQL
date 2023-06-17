from django.urls import path
from shop_recomender.views.user import UserViewCreate, user_redirect, home
from shop_recomender.views.product import ProductView
from shop_recomender.views.admin_view import AdminView
from shop_recomender.views.login import login_view

app_name = 'user'

urlpatterns = [
    path('', home, name='home'),
    path('reg', UserViewCreate.as_view(), name='regiestration'),
    path('redirect/', user_redirect, name='redirection'),
    path('login/', login_view, name='login')
]