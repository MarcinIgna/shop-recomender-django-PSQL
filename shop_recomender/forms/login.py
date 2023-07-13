from django import forms
from shop_recomender.models.user import User


class UserFromLogin(forms.Form):
    username = forms.CharField(       
        label="Username",
        widget=forms.TextInput(
        attrs={"placeholder": "Enter your username"}
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.TextInput(
        attrs={"placeholder": "Enter your username"}
        )
    )
