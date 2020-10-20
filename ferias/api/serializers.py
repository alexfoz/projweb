from rest_framework.serializers import ModelSerializer
from ferias.models import Ferias



class FeriasSerializer(ModelSerializer):
    class Meta:
        model = Ferias
        fields = ['solicitante', 'aprovador', 'justificativa', 'descricao', 'inicio', 'fim']