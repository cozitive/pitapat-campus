from django.db import models

from . import UnsignedAutoField
from .college import College


class Major(models.Model):
    id = UnsignedAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    college = models.ForeignKey(
        College,
        on_delete=models.RESTRICT,
        related_name='majors',
    )

    reg_dt = models.DateTimeField(auto_now_add=True)
    reg_id = models.CharField(max_length=50)
    upd_dt = models.DateTimeField(auto_now=True)
    upd_id = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.college} {self.name}'
