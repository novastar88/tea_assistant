from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class Container(models.Model):
    name = models.CharField(max_length=200, unique=True)
    capacity = models.IntegerField(help_text="in ml")

    def __str__(self) -> str:
        return "".join([self.name, " (", str(self.capacity), " ml)"])


class Product(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(
        max_digits=11, decimal_places=10, default=0)

    rating = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(0)], default=0)
    container_symbol = models.CharField(max_length=5, null=True, blank=True)
    last_used = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(
        to=Status, null=True, blank=True, on_delete=models.PROTECT, related_name="product_status")
    short_description = models.CharField(max_length=50, null=True, blank=True)

    shop_product_link = models.URLField(null=True, blank=True)
    shop = models.ForeignKey(
        to=Company, null=True, blank=True, on_delete=models.PROTECT, related_name="product_shop")

    created_at = models.DateTimeField(
        auto_now_add=True, editable=False)

    def __str__(self) -> str:
        fields = [self, self.status, self.shop]
        return " | ".join([item.name for item in fields if item != None])
