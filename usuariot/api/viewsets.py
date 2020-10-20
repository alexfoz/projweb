from rest_framework.viewsets import ModelViewSet
from usuariot.models import Usuariot
from .serializers import UsuariotSerializer

class UsuariotViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Usuariot.objects.all()
    serializer_class = UsuariotSerializer