# Generated by Django 5.0.3 on 2024-04-07 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_product_shop_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='first_purchased_at',
            new_name='created_at',
        ),
    ]
