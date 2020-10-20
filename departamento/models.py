from django.db import models


# Create your models here.


class Departamento(models.Model):
    departamento = models.TextField(max_length=40)

    def __str__(self):
        return self.departamento
