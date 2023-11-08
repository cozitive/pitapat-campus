from django.db import models

from .custom_field.unsigned_auto_field import UnsignedAutoField
from .user import User


class Photo(models.Model):
    id = UnsignedAutoField(primary_key=True)
    user = models.ForeignKey(User, models.CASCADE, related_name='photos')
    name = models.ImageField(max_length=50)
    path = models.CharField(max_length=256) # unused?
    reg_dt = models.DateTimeField(auto_now_add=True)
    reg_id = models.CharField(max_length=50)
    upd_dt = models.DateTimeField(auto_now=True)
    upd_id = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.path}/{self.name}'
