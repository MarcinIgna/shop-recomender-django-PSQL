from django import forms
from shop_recomender.models.user import User


class UserFrom(forms.Form):
    name = forms.CharField(
        label="Full name",
        min_length=3,
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Input your full name"}
            )
        
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"placeholder": "Enter your email address"}
        )
    )
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
