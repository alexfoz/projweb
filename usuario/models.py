from datetime import date
from django.db import models
from cargo.models import Cargo
from departamento.models import Departamento



# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=8)
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    dataDeNascimento = models.DateField(max_length=10)
    dataDeAdmissao = models.DateField(max_length=10)
    dataDeTermino: date = models.DateField(null=True)
    matricula = models.CharField(max_length=8)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
