from django.db import models

from products.models import Product
from accounts.models import User


class WishlistItem(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' wants ' + str(self.product)