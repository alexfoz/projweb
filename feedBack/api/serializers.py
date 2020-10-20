from rest_framework.serializers import ModelSerializer
from feedBack.models import Feedback



class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['nome', 'usuarioId', 'responsavel', 'descricao', 'data']