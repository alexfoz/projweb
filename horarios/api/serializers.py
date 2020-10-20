from rest_framework.serializers import ModelSerializer
from horarios.models import Horarios



class HorariosSerializer(ModelSerializer):
    class Meta:
        model = Horarios
        fields = ['horario', 'entrada', 'saida', 'intervaloInicio', 'intervaloFim', 'departamentoId']