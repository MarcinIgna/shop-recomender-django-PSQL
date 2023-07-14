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
    success_url = reverse_lazy('user:redirection')

    def form_valid(self, form):
        # Create a new user instance and save it
        user = User.objects.create_user(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        # Redirect to the success URL
        return redirect(self.get_success_url())
# class UserViewCreate(FormView):
#     template_name = 'user/user_regiestration.html'
#     form_class = UserFrom
    
#     def get_success_url(self) -> str:
#         return reverse_lazy('user:redirection')
    
#     def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
#         return super().post(request, *args, **kwargs)
    
#     def form_valid(self, form: User) -> HttpResponse:
#         user = User.objects.create(**form.cleaned_data)
#         return super().form_valid(form)
    
   
def shop(request):
    products = Product.objects.all()
    print("Number of products:", products.count())
    context = {"products": products}
    return TemplateResponse(request, "user/shop.html", context)




def add_to_basket(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        print("add to basket: ",request.session.get('my_user_id'))
        if request.session.get('my_user_id'):
            user_id = request.session.get('my_user_id')
            basket, created = Basket.objects.get_or_create(user_id=user_id)
            basket.products.add(product)
            return JsonResponse({'message': 'Product added to basket.'})
        else:
            return JsonResponse({'message': 'User not authenticated.'}, status=401)
    
    return JsonResponse({'message': 'Invalid request.'}, status=400)



def basket_view(request):
    user_id = request.session.get('my_user_id')
    try:
        basket = Basket.objects.get(user_id=user_id)
        products = basket.products.all()
        total_price = basket.calculate_total_price()
        return render(request, 'user/basket.html', {'products': products, 'total_price': total_price})
    except Basket.DoesNotExist:
        products = []
        total_price = 0
        return render(request, 'user/basket.html', {'products': products, 'total_price': total_price})




def checkout(request):
    user_id = request.session.get('my_user_id')
    basket = Basket.objects.get(user_id=user_id)
    products = basket.products.all()
    total_price = basket.calculate_total_price()
    
    # Perform the necessary logic to process the checkout
    # Calculate the total price, create an order, etc.
    
    # Create the order
    for product in products:
        order = Order.objects.create(user_id=user_id, product=product, total_price=total_price)
    
    # Clear the user's basket after checkout
    basket.products.clear()
    
    # Redirect to a thank you page or a confirmation page after checkout
    return redirect('user:thx')




def logout_view(request):
    logout(request)
    return redirect('user:home')  # Replace 'user:home' with the appropriate URL name for your home page


def thx(request):
    return render(request, 'user/thx.html', {})


