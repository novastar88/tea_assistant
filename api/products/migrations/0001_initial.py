# Generated by Django 5.0.3 on 2024-04-03 21:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=10, default=0, max_digits=11)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('container_symbol', models.CharField(blank=True, max_length=5, null=True)),
                ('last_used', models.DateTimeField(blank=True, null=True)),
                ('short_description', models.CharField(blank=True, max_length=50, null=True)),
                ('shop_product_link', models.URLField(blank=True, null=True)),
                ('first_purchased_at', models.DateTimeField(auto_now_add=True)),
                ('shop_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.company')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.status')),
            ],
        ),
    ]
