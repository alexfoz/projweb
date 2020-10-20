from django.contrib.auth.models import User
from django.db import models
from usuario.models import Usuario


# Create your models here.

class Ausencia(models.Model):
    descricao = models.TextField()
    inicio = models.DateField(max_length=10)
    Fim = models.DateField(max_length=10)
    funcionarioId = models.ForeignKey(User, on_delete=models.CASCADE)
    nome: Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
