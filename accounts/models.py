from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField()
    username = models.CharField(
        max_length=45
        )
    full_name = models.CharField(
        max_length=150
        )