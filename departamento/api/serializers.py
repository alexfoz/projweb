from rest_framework.serializers import ModelSerializer
from departamento.models import Departamento



class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['departamento']