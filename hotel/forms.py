from django import forms
from .models import Product

class CreatProduct(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    malumot = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    price = forms.IntegerField(widget=forms.TextInput({"class": "form-control", "type": "number"}))
    
    class Meta:
        model = Product
        fields = ('name','malumot', 'price','category','image')
