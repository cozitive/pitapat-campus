from django.db import models

from .fields import UnsignedAutoField
from .university import University


class College(models.Model):
    id = UnsignedAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    university = models.ForeignKey(
        University,
        on_delete=models.RESTRICT,
        related_name='colleges',
    )
    reg_dt = models.DateTimeField(auto_now_add=True)
    reg_id = models.CharField(max_length=50)
    upd_dt = models.DateTimeField(auto_now=True)
    upd_id = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.university} {self.name}'
