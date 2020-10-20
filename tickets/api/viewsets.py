from rest_framework.viewsets import ModelViewSet
from tickets.models import Tickets
from .serializers import TicketsSerializer

class TicketsViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer