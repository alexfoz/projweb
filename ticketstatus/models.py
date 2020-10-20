from django.db import models


# Create your models here.
class TicketStatus(models.Model):
    estatus = models.CharField(max_length=50)

    def __str__(self):
        return self.estatus
