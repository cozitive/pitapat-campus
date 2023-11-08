from django.db import models

from pitapat.models.custom_field.unsigned_auto_field import UnsignedAutoField
from pitapat.models.chatroom import Chatroom
from pitapat.models.user import User


class UserChatroom(models.Model):
    key = UnsignedAutoField(primary_key=True)
    user = models.OneToOneField(User, models.CASCADE)
    chatroom = models.ForeignKey(Chatroom, models.CASCADE)

    def __str__(self):
        return f'user {self.user.key} - chatroom {self.chatroom.key}'

    class Meta:
        unique_together = (('user', 'chatroom'),)
