from django.db import models

from pitapat.models import UnsignedAutoField
from pitapat.models.chatroom import Chatroom
from pitapat.models.user import User


class UserChatroom(models.Model):
    id = UnsignedAutoField(primary_key=True)
    user = models.OneToOneField(User, models.CASCADE)
    chatroom = models.ForeignKey(Chatroom, models.CASCADE)

    def __str__(self):
        return f'user {self.user.id} - chatroom {self.chatroom.id}'

    class Meta:
        unique_together = (('user', 'chatroom'),)
