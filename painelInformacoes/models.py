from django.db import models
from django.db.models import TextField


class PainelInformacoes(models.Model):


    descricao: TextField = models.TextField()
    dataCriacao = models.DateField(max_length=12)

    def __str__(self):
        return self.descricao
