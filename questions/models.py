from django.db import models

from products.models import Product
from accounts.models import User


class Question(models.Model):
    objects = models.Manager()

    title = models.CharField('Title', max_length=50)
    question = models.CharField('Question', max_length=5000)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_questions')

    def __str__(self):
        return str(self.user) + str(self.product) + str(self.title)


class Reply(models.Model):
    objects = models.Manager()

    text = models.CharField('Text', max_length=5000)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_replies')

    def __str__(self):
        return str(self.user) + str(self.text)