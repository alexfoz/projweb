from rest_framework.serializers import ModelSerializer
from painelInformacoes.models import PainelInformacoes



class PainelInformacoesSerializer(ModelSerializer):
    class Meta:
        model = PainelInformacoes
        fields = ['dataCriacao', 'descricao']