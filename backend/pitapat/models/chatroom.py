from django.db import models

from .fields import UnsignedAutoField


class Chatroom(models.Model):
    id = UnsignedAutoField(primary_key=True)
    user_count = models.IntegerField(null=False)
    reg_dt = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f'chatroom {self.id}'
