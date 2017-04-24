from django.contrib.auth.models import User, Group
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework_json_api.metadata import JSONAPIMetadata
from rest_framework_json_api.parsers import JSONParser
from rest_framework_json_api.renderers import JSONRenderer

from .models import Network, Node, Sensor, Feature
from .serializers import NetworkSerializer, NodeSerializer, SensorSerializer
from .serializers import FeatureSerializer, UserSerializer, GroupSerializer


class View(ModelViewSet):

    renderer_classes = [JSONRenderer]
    metadata_class = JSONAPIMetadata


class NetworkView(View):

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class NodeView(View):

    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class SensorView(View):

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class FeatureView(View):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class UserView(View):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupView(View):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
