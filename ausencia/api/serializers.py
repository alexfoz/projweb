from rest_framework.serializers import ModelSerializer
from ausencia.models import Ausencia



class AusenciaSerializer(ModelSerializer):
    class Meta:
        model = Ausencia
        fields = ['funcionarioId', 'nome', 'descricao', 'inicio', 'Fim']