from django.contrib.auth.models import User, Group
from rest_framework_gis.serializers import GeometryField
from rest_framework_json_api.serializers import CharField, JSONField, PrimaryKeyRelatedField
from rest_framework_json_api.serializers import ModelSerializer, ResourceRelatedField

from .models import Network, Node, Sensor, Feature

location_help_text = '''
Point represented by GeoJSON, WKT EWKT or HEXEWKB<br><br>
GeoJSON<br>
<pre>
{
    "type": "Point",
    "coordinates": [
        -87.67776489257812,
        41.86137915587359
    ]
}
</pre>'''


observed_properties_help_text = '''
A mapping of the names of values sensors report to properties on features of
interest<br><br>
Ex: your sensor reports internal temperature as something called 'heat_value'
<pre>
{
    "internal_heat": "temperature.internal_temperature"
}
</pre>
'''


class NetworkSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Network


class NodeSerializer(ModelSerializer):
    class Meta:
        fields = ('sensor_network', 'id', 'location', 'sensors', 'info')
        model = Node

    id = CharField()
    sensor_network = PrimaryKeyRelatedField(queryset=Network.objects)
    location = GeometryField(help_text=location_help_text)
    sensors = PrimaryKeyRelatedField(queryset=Sensor.objects, many=True)
    info = JSONField(help_text='JSON for miscellaneous things about the node')


class SensorSerializer(ModelSerializer):
    class Meta:
        fields = ('name', 'observed_properties', 'info')
        model = Sensor

    observed_properties = JSONField(help_text=observed_properties_help_text)
    info = JSONField(help_text='JSON for miscellaneous things about the sensor')

    def validate(self, data):
        Sensor(**data).clean()
        return data


class FeatureSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Feature

    def validate(self, data):
        Feature(**data).clean()
        return data


class UserSerializer(ModelSerializer):
    class Meta:
        exclude = ['password']
        model = User


class GroupSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group
