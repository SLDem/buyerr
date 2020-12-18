from django.db import models
from accounts.models import User
from products.models import Product


class Order(models.Model):
    objects: models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_orders')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.user.name + '  ordered  ' + self.product.title