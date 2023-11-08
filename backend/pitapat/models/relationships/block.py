from django.db import models

from pitapat.models import UnsignedAutoField
from pitapat.models.user import User


class Block(models.Model):
    id = UnsignedAutoField(primary_key=True)
    is_from = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        db_column='from',
        related_name='block_sent',
    )
    to = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='block_received',
    )
