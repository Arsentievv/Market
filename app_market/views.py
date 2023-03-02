from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from app_market.cart import Cart
from app_market.forms import ReviewForm, CartForm, UserParametrsForm, DeliveryForm, PayForm
from app_market.models import Item, Review, Category, Order


class MainPageView(generic.TemplateView):
    template_name = 'app_market/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['limited_items'] = Item.objects.filter(limited_edition=True)[0:16]
        return context


class ProductListView(generic.ListView):
    model = Item
    template_name = 'app_market/item_list.html'
    context_object_name = 'item_list'
    paginate_by = 15
    queryset = Item.objects.all()

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartForm
        return context

    def post(self, request, **kwargs):
        cart = Cart(request)
        item = Item.ojects.get(id=kwargs.get('pk'))
        form = CartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(item=item,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return redirect('/market/cart/')


class ProductDetailView(generic.DetailView):
    model = Item
    template_name = 'app_market/item_detail.html'
    context_object_name = 'item_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        context['review_list'] = Review.objects.filter(item_id=self.object.id).all()
        context['review_count'] = Review.objects.filter(item_id=self.object.id).all().count()
        context['buy_form'] = CartForm()
        return context

    def post(self, request, **kwargs):
        item_detail = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.item = self.get_object()
            review.text = form.cleaned_data.get('text')
            review.save()
            return HttpResponseRedirect(f'/market/product_list/{item_detail.id}/')
        cart = Cart(request)
        item = get_object_or_404(Item, id=kwargs.get('pk'))
        cart_form = CartForm(request.POST)
        if cart_form.is_valid():
            cd = cart_form.cleaned_data
            cart.add(item=item,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return render(request, 'app_market/item_detail.html', context={
            'form': form, 'item_detail': item_detail})

class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'app_market/cart_detail.html', {'cart': cart})



class SearchResultView(generic.ListView):
    model = Item
    template_name = 'app_market/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Item.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'app_market/category_list.html'
    context_object_name = 'category_list'


class BuyView(generic.TemplateView):
    template_name = 'app_market/user_param.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserParametrsForm
        context['delivery_form'] = DeliveryForm
        context['pay_form'] = PayForm
        return context

# Убрать item list добавить в историю заказов. Заказ убрать из моделей. Корзину вывести через get_context data
    def post(self, request):
        user_form = UserParametrsForm(request.POST)
        if user_form.is_valid():
            delivery_form = DeliveryForm(request.POST)
            if delivery_form.is_valid():
                delivery = delivery_form.cleaned_data.get('express_delivery')
                if delivery == True:
                    delivery = True
                else:
                    delivery = False
                city = delivery_form.cleaned_data.get('city')

                address = delivery_form.cleaned_data.get('address')
                user = request.user
                cart = Cart(request)
                price = cart.get_total_price()
                if delivery == True:
                    price += 500
                elif cart.get_total_price() < 2000:
                    price += 200
                order = Order.objects.create(
                    user=user, express_delivery=delivery, city=city, address=address, price=price

                )
                order.save()
                pay_form = PayForm(request.POST)
                if pay_form.is_valid():
                    return HttpResponseRedirect(f'/market/order/{order.id}/')


class OrderView(generic.DetailView):
    model = Order
    template_name = 'app_market/order.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context









