from django.contrib.auth.models import User
from django.db import models
from tickets.models import Tickets
from usuario.models import Usuario


# Create your models here.

class Usuariot(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticketId = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    dataUltimaAlteracao = models.DateField(max_length=10)
    solicitado = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.solicitante)
