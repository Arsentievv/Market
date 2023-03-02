from django.urls import path

from app_market.views import CartView
from .views import (
    RegistrationView,
    Login,
    Logout,
    MyAcoountView,
    ProfileUpdateView,

)


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('my_account/<int:pk>', MyAcoountView.as_view(), name='my_account'),
    path('my_account/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('cart/', CartView.as_view(), name='cart'),

]