from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .chatroom import Chatroom
from .college import College
from .custom_field.unsigned_auto_field import UnsignedAutoField
from .major import Major
from .pitapat_user_manager import PitapatUserManager
from .university import University


class BaseUser(AbstractBaseUser, PermissionsMixin):
    key = UnsignedAutoField(primary_key=True, db_column='user_key')
    email = models.EmailField(unique=True, max_length=50)

    reg_dt = models.DateTimeField(auto_now_add=True)
    reg_id = models.CharField(max_length=50)
    upd_dt = models.DateTimeField(auto_now=True)
    upd_id = models.CharField(max_length=50)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = PitapatUserManager()

    def __str__(self):
        return self.email


class User(BaseUser):
    university = models.ForeignKey(University, models.RESTRICT)
    college = models.ForeignKey(College, models.RESTRICT)
    major = models.ForeignKey(Major, models.RESTRICT)

    nickname = models.CharField(null=False, max_length=30)
    phone = models.CharField(null=True, max_length=20)
    status = models.CharField(max_length=1)
    gender = models.CharField(max_length=1)
    interested_gender = models.CharField(max_length=1)
    birthday = models.DateField()
    tags = models.ManyToManyField('Tag', through='UserTag', through_fields=('user', 'tag'))
    chatrooms = models.ManyToManyField(
        Chatroom,
        through='UserChatroom',
        through_fields=('user', 'chatroom'),
    )
