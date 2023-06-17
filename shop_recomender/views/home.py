from django.shortcuts import render

def home_base(request):
    return render(request, 'user/home.html')