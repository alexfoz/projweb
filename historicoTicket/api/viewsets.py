from rest_framework.viewsets import ModelViewSet
from historicoTicket.models import HistoricoTicket
from .serializers import HistoricoticketSerializer

class HistoricoticketViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = HistoricoTicket.objects.all()
    serializer_class = HistoricoticketSerializer