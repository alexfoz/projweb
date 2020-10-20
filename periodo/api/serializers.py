from rest_framework.serializers import ModelSerializer
from periodo.models import Periodo



class PeriodoSerializer(ModelSerializer):
    class Meta:
        model = Periodo
        fields = ['escala', 'data', 'turno']