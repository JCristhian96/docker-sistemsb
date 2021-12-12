from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Managers
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Modelo para los Usuarios
    """
    username = models.CharField(
        max_length=255,
        unique=True
    )
    email = models.EmailField(
        unique=True
    )
    name = models.CharField(
        'Nombres',
        max_length=255,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        'Apellidos',
        max_length=255,
        blank=True,
        null=True
    )
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def natural_key(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return f'{self.name} {self.last_name}'
