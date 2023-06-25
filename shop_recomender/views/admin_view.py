from django.template.response import TemplateResponse
from shop_recomender.models.user import User
from shop_recomender.models.product import Product
from django.views.generic import FormView
from django.http import HttpRequest, HttpResponse
from typing import Any
class AdminView(FormView):
    @staticmethod
    def see_all_users(request):
        users = User.objects.all()
        context = {"users": users}
        # print(users.query)
        return TemplateResponse(request, "admin/all_users.html", context)
    @staticmethod
    def see_all_products(request):
        products = Product.objects.all()
        context = {"products": products}
        return TemplateResponse(request, "product/all_products.html", context)


    
    