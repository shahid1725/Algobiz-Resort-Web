
from django import forms
from django.forms import ModelForm
from head.models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name","price","image","location"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }

        labels = {
            'name': 'Product Name',
            "price": "Price",
        }