from rest_framework.viewsets import ModelViewSet
from horarios.models import Horarios
from .serializers import HorariosSerializer

class HorariosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializer