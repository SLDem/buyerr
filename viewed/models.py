from django.db import models


class ViewedItem(models.Model):
    objects = models.Manager()

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' viewed ' + str(self.product)
