from django.contrib.auth.models import User, Group
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework_json_api.views import ModelViewSet
from rest_framework_json_api.metadata import JSONAPIMetadata
from rest_framework_json_api.renderers import JSONRenderer
from rest_framework_json_api.parsers import JSONParser

from .models import Network, Node, Sensor, Feature
from .serializers import NetworkSerializer, NodeSerializer, SensorSerializer
from .serializers import FeatureSerializer, UserSerializer, GroupSerializer


class NetworkView(ModelViewSet):

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class NodeView(ModelViewSet):

    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class SensorView(ModelViewSet):

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class FeatureView(ModelViewSet):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class UserView(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupView(ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
