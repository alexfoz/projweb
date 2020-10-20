from rest_framework.viewsets import ModelViewSet
from periodo.models import Periodo
from .serializers import PeriodoSerializer

class PeriodoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer