from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self, name, email, username, password=None):
        if not username:
            raise ValueError('The Username must be set')

        user = self.model(
            name=name,
            email=self.normalize_email(email),
            username=username,
        )

        user.password = make_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, username, password):
        user = self.create_user(
            name=name,
            email=email,
            username=username,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255, default='Unknown')
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    registration_date = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin