from django.db import models

from .custom_field.unsigned_auto_field import UnsignedAutoField


class Chatroom(models.Model):
    key = UnsignedAutoField(primary_key=True)
    user_count = models.IntegerField(null=False)
    reg_dt = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return f'chatroom {self.key}'
