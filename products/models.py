from django.db import models


class Category(models.Model):
    objects = models.Manager()

    image = models.ImageField(upload_to='images', null=True)
    title = models.CharField(max_length=200, unique=True, blank=False, null=False)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=200, unique=True, blank=False)

    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=400, unique=False, blank=False, null=False)
    description = models.CharField(max_length=4000, blank=False, null=False)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    sub_category = models.ForeignKey(SubCategory,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     blank=True,
                                     related_name='products')

    def __str__(self):
        return self.title


class Image(models.Model):
    objects = models.Manager()

    image = models.ImageField(upload_to='images', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images', null=True)

    def __str__(self):
        return 'image for ' + self.product.title + str(self.pk)

