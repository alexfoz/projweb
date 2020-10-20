from rest_framework.serializers import ModelSerializer
from tickets.models import Tickets



class TicketsSerializer(ModelSerializer):
    class Meta:
        model = Tickets
        fields = ['user', 'assunto', 'descricao', 'dataCriacao', 'dataFim', 'estatus']