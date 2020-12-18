from django.db import models

from accounts.models import User


class Rating(models.Model):
    objects = models.Manager()

    value = models.IntegerField(default=1)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_ratings_posted')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_ratings_received')
