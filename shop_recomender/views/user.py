from typing import Any
from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import FormView
from django.template.response import TemplateResponse
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from shop_recomender.models.order import Order
from shop_recomender.models.basket import Basket
from shop_recomender.models.product import Product
from shop_recomender.models.user import User
from shop_recomender.froms.user import UserFrom



def home(request: WSGIRequest) -> HttpResponse:
    return TemplateResponse(request, 'user/home.html', {})


def user_redirect(request: WSGIRequest) -> HttpResponse:
    return TemplateResponse(request, 'user/redirect.html', {})



class UserViewCreate(FormView):
    template_name = 'user/user_regiestration.html'
    form_class = UserFrom
    
    def get_success_url(self) -> str:
        return reverse_lazy('user:redirection')
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form: User) -> HttpResponse:
        user = User.objects.create(**form.cleaned_data)
        return super().form_valid(form)
    
   
def shop(request):
    products = Product.objects.all()
    print("Number of products:", products.count())
    context = {"products": products}
    return TemplateResponse(request, "user/shop.html", context)




def add_to_basket(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        
        # Retrieve or create the user's basket
        basket, created = Basket.objects.get_or_create(
            user_id=request.session.get('my_user_id')
            )
        
        # Add the product to the user's basket
        basket.products.add(product)
        
        return JsonResponse({'message': 'Product added to basket.'})
    
    return JsonResponse({'message': 'Invalid request.'}, status=400)


def checkout(request):
    basket = Basket.objects.get(user=request.user)
    products = basket.products.all()
    total_price = basket.calculate_total_price()
    
    # Perform the necessary logic to process the checkout
    # Calculate the total price, create an order, etc.
    
    # Create the order
    order = Order.objects.create(user=request.user, total_price=total_price)
    order.products.set(products)
    
    # Clear the user's basket after checkout
    basket.products.clear()
    
    # Redirect to a thank you page or a confirmation page after checkout
    return redirect('user:checkedout')


def basket_view(request):
    x = request.session.get('my_user_id')
    print("HEREEEERWERWEREWREW",x)
    user = request.user
    basket = Basket.objects.get(user_id=x)
    products = basket.products.all()
    total_price = basket.calculate_total_price()
    return render(request, 'user/basket.html', {'products': products, 'total_price': total_price})


def logout_view(request):
    logout(request)
    return redirect('user:home')  # Replace 'user:home' with the appropriate URL name for your home page


def thx(request):
    return HttpResponse("Thank you for your order!")


