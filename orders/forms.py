from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'product-quantity-input'}))

    class Meta:
        model = Order
        fields = ('quantity', )
