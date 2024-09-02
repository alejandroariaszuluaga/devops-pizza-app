from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['pizza_type', 'comments']
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
