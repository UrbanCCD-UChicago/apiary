from django.contrib.auth.models import User, Group
from rest_framework_json_api.serializers import ModelSerializer
from .models import Network, Node, Sensor, Feature


class NetworkSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Network


class NodeSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Node


class SensorSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Sensor


class FeatureSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Feature


class UserSerializer(ModelSerializer):
    class Meta:
        exclude = ['password']
        model = User


class GroupSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group
