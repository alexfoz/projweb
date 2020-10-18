from django.db import models
from django.contrib.auth.models import User
from tickets.models import Tickets
from usuario.models import Usuario
from ticketstatus.models import TicketStatus

# Create your models here.

class HistoricoTicket(models.Model):
    ticketId: Tickets = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    usuario_alteracao: Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ultima_aletracao = models.DateField(max_length=20)
    usuario_solicitado: Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estatus: TicketStatus = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.estatus)
