from django import forms

from app_market.models import Review, Order
from app_users.models import Profile


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

class CartForm(forms.Form):
    quantity = forms.IntegerField()
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class UserParametrsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'surname', 'last_name', 'phone_numb', 'email']

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['city', 'address', 'express_delivery']