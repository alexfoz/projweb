from rest_framework.viewsets import ModelViewSet
from painelInformacoes.models import PainelInformacoes
from .serializers import PainelInformacoesSerializer

class PainelInformacoesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PainelInformacoes.objects.all()
    serializer_class = PainelInformacoesSerializer