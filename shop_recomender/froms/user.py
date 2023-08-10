from django import forms
from shop_recomender.models.user import User




class UserFromUpdate(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # If an instance is provided, update the fields with the instance data
            self.fields['name'].initial = self.instance.name
            self.fields['email'].initial = self.instance.email

    def save(self, commit=True):
        # Save the form data to the instance
        instance = super().save(commit=False)
        instance.name = self.cleaned_data['name']
        instance.email = self.cleaned_data['email']
        if self.cleaned_data['password']:
            instance.set_password(self.cleaned_data['password'])
        if commit:
            instance.save()
        return instance


class UserFrom(forms.Form):
    # for user registration
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
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter your password"}
        )
)

