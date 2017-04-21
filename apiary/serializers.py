from rest_framework_json_api.serializers import ModelSerializer
from .models import Network


class NetworkSerializer(ModelSerializer):
    fields = '__all__'
    class Meta:
        model = Network
