from rest_framework.serializers import ModelSerializer
from usuariot.models import Usuariot



class UsuariotSerializer(ModelSerializer):
    class Meta:
        model = Usuariot
        fields = ['ticketId', 'solicitante', 'dataUltimaAlteracao', 'solicitado']