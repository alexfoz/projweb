from django.db import models
from escala.models import Departamento

# Create your models here.

class Periodo(models.Model):
    data = models.DateField(max_length=10)
    escala = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    turno = models.TextField(max_length=20)

    def __str__(self):
        return self.Turno


