from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager

from .college import College
from .major import Major
from .university import University


class PitapatUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(nickname=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, nickname, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(nickname, email, password, **extra_fields)

    def create_superuser(self, nickname, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            nickname,
            email,
            password,
            university=University.objects.get(name="admin"),
            college=College.objects.get(name="admin"),
            major=Major.objects.get(name="admin"),
            birthday=datetime.now(),
            **extra_fields,
        )
