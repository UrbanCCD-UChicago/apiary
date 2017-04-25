from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db.models import CharField, ForeignKey, ManyToManyField
from django.contrib.gis.db.models import PointField, Model, DO_NOTHING


class Network(Model):
    name = CharField(primary_key=True, max_length=255)
    info = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__network_metadata'


class Node(Model):
    id = CharField(primary_key=True, max_length=255)
    sensor_network = ForeignKey(Network, DO_NOTHING, db_column='sensor_network')
    location = PointField(blank=True, null=True)
    info = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__node_metadata'
        unique_together = (('id', 'sensor_network'),)


class Sensor(Model):
    name = CharField(primary_key=True, max_length=255)
    observed_properties = JSONField(blank=True, null=True)
    info = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__sensor_metadata'


class Feature(Model):
    name = CharField(primary_key=True, max_length=255)
    observed_properties = JSONField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'sensor__feature_metadata'


class SensorFeatureToNetwork(Model):
    feature = ForeignKey(Feature, DO_NOTHING, db_column='feature', blank=True, null=True)
    network = ForeignKey(Network, DO_NOTHING, db_column='network', blank=True, null=True)

    class Meta:
        db_table = 'sensor__feature_to_network'


class SensorSensorToNode(Model):
    sensor = ForeignKey(Sensor, DO_NOTHING, db_column='sensor', blank=True, null=True)
    network = ForeignKey(Node, DO_NOTHING, db_column='network', blank=True, null=True)
    node = CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'sensor__sensor_to_node'
