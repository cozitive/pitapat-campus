from django.db import models

from .custom_field.unsigned_auto_field import UnsignedAutoField
from .user import User


class Introduction(models.Model):
    id = UnsignedAutoField(primary_key=True)
    user = models.OneToOneField(User, models.CASCADE)
    content = models.TextField()
    reg_dt = models.DateTimeField(auto_now_add=True)
    reg_id = models.CharField(max_length=50)
    upd_dt = models.DateTimeField(auto_now=True)
    upd_id = models.CharField(max_length=50)

    def __str__(self):
        return f'introduction of {self.user.email}'
