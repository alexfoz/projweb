from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Cargo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.TextField(max_length=40)

    def __str__(self):
        return self.cargo
