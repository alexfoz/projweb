from django.db import models
from departamento.models import Departamento


# Create your models here.

class Horarios(models.Model):
    horario = models.CharField(max_length=60)
    entrada = models.TimeField(max_length=20)
    saida = models.TimeField(max_length=20)
    intervaloInicio = models.TimeField(default=None, max_length=40)
    intervaloFim = models.TimeField(default=None, max_length=40 )
    departamentoId = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.horario
