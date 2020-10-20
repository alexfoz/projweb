from rest_framework.viewsets import ModelViewSet
from ausencia.models import Ausencia
from .serializers import AusenciaSerializer

class AusenciaViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Ausencia.objects.all()
    serializer_class = AusenciaSerializer