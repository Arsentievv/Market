# Generated by Django 4.1.5 on 2023-02-27 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0010_remove_order_item_order_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app_market.item'),
            preserve_default=False,
        ),
    ]