from rest_framework.serializers import ModelSerializer
from usuario.models import Usuario



class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'nome', 'cpf', 'email', 'telefone', 'dataDeNascimento', 'dataDeAdmissao', 'dataDeTermino', 'matricula', 'cargo', 'departamento']