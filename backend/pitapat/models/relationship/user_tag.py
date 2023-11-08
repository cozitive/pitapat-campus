from django.db import models

from pitapat.models.custom_field.unsigned_auto_field import UnsignedAutoField
from pitapat.models.tag import Tag
from pitapat.models.user import User


class UserTag(models.Model):
    key = UnsignedAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    tag = models.ForeignKey(Tag, on_delete=models.RESTRICT)

    def __str__(self):
        return f'user {self.user.key} - tag {self.tag.key}'

    class Meta:
        unique_together = (('user', 'tag'),)
