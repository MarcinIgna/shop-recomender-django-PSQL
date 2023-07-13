from django.http import HttpResponse
from shop_recomender.models.product import Product
from django.template.response import TemplateResponse
from django.views.generic import FormView
from shop_recomender.forms.product import ProductForm
from django.urls import reverse_lazy

class ProductView(FormView):
    
    template_name = "product/add_product.html"
    form_class = ProductForm
    
    def get_success_url(self) -> str:
        return reverse_lazy('user:redirection')
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        product = Product.objects.create(**form.cleaned_data)
        return super().form_valid(form)
    
