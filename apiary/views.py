from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework_json_api.metadata import JSONAPIMetadata
from rest_framework_json_api.parsers import JSONParser
from rest_framework_json_api.renderers import JSONRenderer

from .models import Network
from .serializers import NetworkSerializer


class View(ModelViewSet):

    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    metadata_class = JSONAPIMetadata


class NetworkView(View):

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
