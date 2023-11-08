from django.db import models

from .chatroom import Chatroom
from .custom_field.unsigned_auto_field import UnsignedAutoField
from .user import User


class Chat(models.Model):
    id = UnsignedAutoField(primary_key=True)
    chatroom = models.ForeignKey(
        Chatroom,
        on_delete=models.CASCADE,
        related_name='chats',
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )
    valid = models.CharField(max_length=1)
    content = models.TextField()
    reg_dt = models.DateTimeField(auto_now_add=True)
    upd_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.nickname}: {self.content}'
