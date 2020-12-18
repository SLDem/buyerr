from django.db import models

from accounts.models import User


class Message(models.Model):
    objects = models.Manager()

    text = models.CharField('Text', max_length=3000)

    sender = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user_sent_messages', null=True)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user_received_messages', null=True)

    def __str__(self):
        return self.text
