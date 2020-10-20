from rest_framework.viewsets import ModelViewSet
from cargo.models import Cargo
from .serializers import CargoSerializer

class CargoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer