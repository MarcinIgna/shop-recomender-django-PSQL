from django.shortcuts import render

from shop_recomender.models.user import User
from django.http import HttpResponse



class UserView():
    @staticmethod
    def add_user():
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user, created= User(name=name, email=email, username=username, password=password)
        user.save()
        if created:
            return HttpResponse("User added successfully")
        else:
            return HttpResponse("Something went wrong")
        #regiestration
    @staticmethod
    def delete_user(request,user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return HttpResponse("User deleted successfully")
        

    