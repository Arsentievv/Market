from django.contrib.auth.models import User
from django.db import models

from app_market.models import Category


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user')
    first_name = models.CharField(max_length=20, verbose_name='First name')
    last_name = models.CharField(max_length=20, verbose_name='Last name')
    surname = models.CharField(max_length=20, verbose_name='Surname')
    phone_numb = models.CharField(max_length=15, unique=True, verbose_name='Phone number')
    avatar = models.ImageField(upload_to='files/avatars/', verbose_name='Avatar')
    email = models.EmailField(verbose_name='Email', unique=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Registration date')
    fave_category = models.ManyToManyField(Category, default=None, null=True)

    def get_upload_url(self):
        return self.avatar.url


