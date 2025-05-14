from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CajeroUserManager(BaseUserManager):
    def create_user(self, pin, saldo=0):
        user = self.model(pin=pin, saldo=saldo)
        user.set_password(str(pin))  # simplificado
        user.save()
        return user

class CajeroUser(AbstractBaseUser):
    pin = models.PositiveIntegerField(unique=True)
    saldo = models.FloatField(default=0)

    USERNAME_FIELD = 'pin'

    objects = CajeroUserManager()

    def __str__(self):
        return f"Usuario {self.pin}"