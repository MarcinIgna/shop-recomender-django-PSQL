from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView
from django.template.response import TemplateResponse
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse_lazy

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
        User.objects.create(**form.cleaned_data)
        return super().form_valid(form)
    