from django.db import models

from .chat import Chat
from .chatroom import Chatroom
from .introduction import Introduction
from .photo import Photo
from .pitapat_user_manager import PitapatUserManager
from .relationships.pitapat import Pitapat
from .relationships.block import Block
from .relationships.user_chatroom import UserChatroom
from .relationships.user_tag import UserTag
from .tag import Tag
from .university import University
from .college import College
from .major import Major
from .user import User


class UnsignedAutoField(models.BigAutoField):
    def db_type(self, connection):
        return 'bigint UNSIGNED AUTO_INCREMENT'

    def rel_db_type(self, connection):
        return 'bigint UNSIGNED'
