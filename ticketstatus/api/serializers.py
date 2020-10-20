from rest_framework.serializers import ModelSerializer
from ticketstatus.models import TicketStatus



class TicketStatusSerializer(ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = ['estatus']