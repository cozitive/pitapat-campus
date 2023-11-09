from django.db import models

from pitapat.models.fields import UnsignedAutoField
from pitapat.models.tag import Tag
from pitapat.models.user import User


class UserTag(models.Model):
    id = UnsignedAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    tag = models.ForeignKey(Tag, on_delete=models.RESTRICT)

    def __str__(self):
        return f'user {self.user.id} - tag {self.tag.id}'

    class Meta:
        unique_together = (('user', 'tag'),)
