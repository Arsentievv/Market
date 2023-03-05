from django.contrib.auth.models import User
from django.db import models



class Item(models.Model):
    title = models.CharField(max_length=30, verbose_name='Item title')
    description = models.TextField(max_length=200, verbose_name='Item description')
    price = models.PositiveIntegerField(verbose_name='Item price')
    sell_amt = models.PositiveIntegerField(default=1, verbose_name='Item amount')
    limited_edition = models.BooleanField(default=None, verbose_name='Limited edition')
    in_stock = models.PositiveIntegerField(default=1, verbose_name='Item in stock')
    img = models.ImageField(null=True, verbose_name='Item Image', upload_to='files/items/')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Day of publishing')
    category = models.ForeignKey('Category', null=True, default=None, on_delete=models.CASCADE)

    def get_upload_url(self):
        return self.img.url

    def get_short_desc(self):
        return self.description[:20]

class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='Product category', default='other')


class FavouriteCategory(models.Model):
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, verbose_name='Text')
    item = models.ForeignKey(Item, default=None, on_delete=models.CASCADE)


class Cart(models.Model):
    cart_id = models.CharField(max_length=50)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, unique=False)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)


class Order(models.Model):
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    express_delivery = models.BooleanField(help_text='Cost: 500$')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, default=None)
    price = models.IntegerField(default=0)




