from rest_framework.viewsets import ModelViewSet
from departamento.models import Departamento
from .serializers import DepartamentoSerializer

class DepartamentoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer