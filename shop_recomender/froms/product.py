from django import forms
from shop_recomender.models.category import Category

class ProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].label_from_instance = lambda obj: obj.name
    name = forms.CharField(
        label="Product name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter product name"
            }
        )
    )
    price = forms.DecimalField()
    description = forms.CharField(
        label="Product description",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter product description"
            }
        )
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name="name")

