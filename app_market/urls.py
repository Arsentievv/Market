from django.urls import path
from .views import (
    MainPageView,
    ProductListView,
    ProductDetailView,
    SearchResultView,
    CategoryListView,
    BuyView,
    OrderView,
)

urlpatterns = [
    path('main/', MainPageView.as_view(), name='main'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_list/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('first_step/', BuyView.as_view(), name='first_step'),
    path('order/<int:pk>/', OrderView.as_view(), name='order'),





]