from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_address', 'phone', 'email']
        widgets = {
            'shipping_address': forms.Textarea(attrs={'rows': 3}),
        }