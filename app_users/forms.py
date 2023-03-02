from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, help_text='Your first name')
    last_name = forms.CharField(max_length=20, help_text='Your last name')
    surname = forms.CharField(max_length=20, help_text='Your surname')
    phone_numb = forms.CharField(max_length=15, required=False, help_text='Your phone number')
    avatar = forms.ImageField(required=False, help_text='Your avatar')
    email = forms.EmailField(help_text='Your email')


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, help_text='Insert your username')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Insert your password')