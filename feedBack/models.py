from django.contrib.auth.models import User
from usuario.models import Usuario
from django.db import models


# Create your models here.


class Feedback(models.Model):
    descricao = models.TextField()
    data = models.DateField(null=True)
    responsavel = models.CharField(max_length=50)
    usuarioId = models.ForeignKey(User, on_delete=models.CASCADE)
    nome: Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    #@property
    def __str__(self):
        return str(self.nome)




