from collections import defaultdict
from django.contrib.auth.models import User, Group
from rest_framework_json_api.serializers import ModelSerializer
from rest_framework_json_api.serializers import ValidationError
from .models import Network, Node, Sensor, Feature
from .validators import validate_sensor, validate_feature


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

    def validate(self, data):
        return validate_sensor(data)


class FeatureSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Feature

    def validate(self, data):
        return validate_feature(data)


class UserSerializer(ModelSerializer):
    class Meta:
        exclude = ['password']
        model = User


class GroupSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group
