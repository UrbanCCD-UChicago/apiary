from apiary.models import Network, Node, Feature, Sensor
from apiary.validators import validate_feature
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db.models import CharField, ForeignKey, Model
from django.contrib.gis.db.models import CASCADE,DO_NOTHING


class SensorFeatureToNetwork(Model):
    feature = ForeignKey(Feature, on_delete=CASCADE, db_column='feature')
    network = ForeignKey(Network, on_delete=CASCADE, db_column='network')

    class Meta:
        db_table = 'sensor__feature_to_network'
        managed = False


class SensorSensorToNode(Model):
    sensor = ForeignKey(Sensor, on_delete=CASCADE, db_column='sensor')
    network = ForeignKey(Node, on_delete=CASCADE, db_column='network')
    node = CharField(max_length=255)

    class Meta:
        db_table = 'sensor__sensor_to_node'
        managed = False
