from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Usuario', max_length=20, unique=True)
    email = models.EmailField('Correo', unique=True)
    name = models.CharField("Nombre", max_length=30)
    last_name = models.CharField("Apellido", max_length=30)

    USERNAME_FIELD = 'usename'

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def ger_full_name(self):
        return f"{self.name} - {self.last_name}"
    
    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

