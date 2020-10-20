from django.contrib.auth.models import User
from django.db import models
from ticketstatus.models import TicketStatus


class Tickets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assunto = models.TextField(max_length=140)
    descricao = models.TextField()
    dataCriacao = models.DateField(max_length=12)
    dataFim = models.DateField(max_length=12)
    estatus: TicketStatus = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.assunto
