from rest_framework.serializers import ModelSerializer
from escala.models import Escala



class EscalaSerializer(ModelSerializer):
    class Meta:
        model = Escala
        fields = ['departamentoId', 'turno']