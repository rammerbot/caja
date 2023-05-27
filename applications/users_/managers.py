from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager,models.Manager):

    def _create_user(self, username,email,name, last_name, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name, 
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username,email,name, last_name, password=None, **extra_fields):
        return self._create_user(username,email,name, last_name, password, True, False, True, **extra_fields)


    def create_superuser(self, username,email,name, last_name, password=None, **extra_fields):
        return self._create_user(username,email,name, last_name, password, True, True, True, **extra_fields)
