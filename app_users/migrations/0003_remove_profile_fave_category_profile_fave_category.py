# Generated by Django 4.1.5 on 2023-02-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0008_remove_category_item_item_category'),
        ('app_users', '0002_profile_fave_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fave_category',
        ),
        migrations.AddField(
            model_name='profile',
            name='fave_category',
            field=models.ManyToManyField(default=None, null=True, to='app_market.category'),
        ),
    ]
