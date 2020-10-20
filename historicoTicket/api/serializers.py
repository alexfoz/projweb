from rest_framework.serializers import ModelSerializer
from historicoTicket.models import HistoricoTicket



class HistoricoticketSerializer(ModelSerializer):
    class Meta:
        model = HistoricoTicket
        fields = ['ticketId', 'usuario_alteracao', 'ultima_alteracao', 'usuario_solicitado', 'estatus']