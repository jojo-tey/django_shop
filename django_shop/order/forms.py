from django import forms
from .models import Order
from product.models import Product
from user.models import User


class RegisterForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(error_messages={
        'required': 'Please enter quantity'
    }, label="Quantity")

    product = forms.IntegerField(error_messages={
        'required': 'Please write product description'}, label='Product description', widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.session.get('user')

        if not (quantity and product):
            self.add_error('quantity', 'No result')
            self.add_error('product', 'No result')
