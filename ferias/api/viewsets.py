from rest_framework.viewsets import ModelViewSet
from ferias.models import Ferias
from .serializers import FeriasSerializer

class FeriasViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Ferias.objects.all()
    serializer_class = FeriasSerializer