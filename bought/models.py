from django.db import models

from products.models import Product
from accounts.models import User


class BoughtProduct(models.Model):
    objects = models.Manager()

    quantity = models.IntegerField(default=1)

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bought_products')
