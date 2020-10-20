from rest_framework.viewsets import ModelViewSet
from escala.models import Escala
from .serializers import EscalaSerializer

class EscalaViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Escala.objects.all()
    serializer_class = EscalaSerializer