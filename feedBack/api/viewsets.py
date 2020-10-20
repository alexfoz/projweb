from rest_framework.viewsets import ModelViewSet
from feedBack.models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer