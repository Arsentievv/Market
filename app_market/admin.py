from django.contrib import admin

from app_market.models import Item, Category


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'sell_amt', 'limited_edition', 'in_stock', 'img']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
