from rest_framework.serializers import ModelSerializer
from cargo.models import Cargo



class CargoSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['user', 'cargo']