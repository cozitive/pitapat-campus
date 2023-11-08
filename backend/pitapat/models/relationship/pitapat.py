from django.db import models

from pitapat.models.custom_field.unsigned_auto_field import UnsignedAutoField
from pitapat.models.user import User


class Pitapat(models.Model):
    key = UnsignedAutoField(primary_key=True)
    is_from = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        db_column='from',
        related_name='pitapat_sent',
    )
    to = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='pitapat_received',
    )
