from rest_framework.viewsets import ModelViewSet
from ticketstatus.models import TicketStatus
from .serializers import TicketStatusSerializer

class TicketStatusViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer