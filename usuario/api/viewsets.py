from rest_framework.viewsets import ModelViewSet
from usuario.models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer