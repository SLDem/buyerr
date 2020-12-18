from django.db import models

from accounts.models import User


class Review(models.Model):
    objects = models.Manager()

    text = models.CharField('Text', max_length=3000)
    pluses = models.CharField('Pluses', max_length=5000)
    minuses = models.CharField('Minuses', max_length=5000)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_reviewed')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')

    def __str__(self):
        return self.text