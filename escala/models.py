from django.contrib.auth.models import User
from django.db import models
from departamento.models import Departamento


# Create your models here.

class Escala(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turno = models.TextField(max_length=20)
    departamentoId: Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.turno)
