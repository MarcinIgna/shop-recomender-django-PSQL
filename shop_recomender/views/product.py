from django.http import HttpResponse
from shop_recomender.models.product import Product
from django.template.response import TemplateResponse

class ProductView():
    @staticmethod
    def add_product():
        name = input("Enter your name: ")
        price = input("Enter your price: ")
        description = input("Enter your description: ")
        category_id = input("Enter your category_id: ")
        product, created= Product(name=name, price=price, description=description, category_id=category_id)
        product.save()
        if created:
            return HttpResponse("Product added successfully")
        else:
            return HttpResponse("Something went wrong")
    @staticmethod
    def delete_product(request,product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return HttpResponse("Product deleted successfully")
        
    @staticmethod
    def update_product(request,product_id):
        product = Product.objects.get(id=product_id)
        name = input("Enter your name: ")
        price = input("Enter your price: ")
        description = input("Enter your description: ")
        product.name = name
        product.price = price
        product.description = description
        product.save()
        return HttpResponse("Product updated successfully")
        
    @staticmethod
    def get_product(request,product_id):
        product = Product.objects.get(id=product_id)
        context = {"product": product}
        return TemplateResponse(request, "product.html", context)
        
    @staticmethod
    def get_all_products(request):
        products = Product.objects.all()
        query_statement = products.query
        print(query_statement)
        context = {"product": products}
        return TemplateResponse(request, "all_products.html", context)