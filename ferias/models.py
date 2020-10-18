from django.db import models
from django.contrib.auth.models import User
from usuario.models import Usuario



class Ferias(models.Model):
    inicio = models.DateField(max_length=20)
    fim = models.DateField(max_length=20)
    descricao = models.CharField(max_length=240)
    justificativa = models.CharField(max_length=480)
    solicitante: Usuario = models.ForeignKey(Usuario, default=str, on_delete=models.CASCADE)
    aprovador = models.ForeignKey(User, default=str, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.solicitante)
