from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework_json_api.views import ModelViewSet
from rest_framework_json_api.metadata import JSONAPIMetadata
from rest_framework_json_api.renderers import JSONRenderer
from rest_framework_json_api.parsers import JSONParser

from .forms import NodeForm
from .models import Network, Node, Sensor, Feature, SensorSensorToNode
from .serializers import NetworkSerializer, NodeSerializer, SensorSerializer
from .serializers import FeatureSerializer, UserSerializer, GroupSerializer


def index(request):
    return render(request, 'index.html')


def register_node(request):
    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.method == 'POST':
        form = NodeForm(request.POST)
    else:
        form = NodeForm()

    data = {
        'form': form
    }

    return render(request, 'register_node.html', data)


class NetworkView(ModelViewSet):

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class NodeView(ModelViewSet):

    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        network_id = serializer.data['sensor_network']['id']
        network = Network.objects.get(pk=network_id)
        node_id = serializer.data['id']
        node_location = str(serializer.data['location'])
        node_info = serializer.data['info']

        node = Node.objects.create(id=node_id, sensor_network=network, location=node_location, info=node_info)

        for sensor in serializer.data['sensors']:
            sensor = Sensor.objects.get(pk=sensor['id'])
            SensorSensorToNode.objects.create(node=node, sensor=sensor, network=network)

        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)



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
