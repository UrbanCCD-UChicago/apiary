from apiary.validators import validate_feature
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db.models import CharField, ForeignKey, ManyToManyField
from django.contrib.gis.db.models import PointField, Model, DO_NOTHING


class Network(Model):
    name = CharField(primary_key=True, max_length=255)
    info = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__network_metadata'

    def __str__(self):
        return self.name


class Node(Model):
    id = CharField(primary_key=True, max_length=255)
    sensor_network = ForeignKey(Network, DO_NOTHING, db_column='sensor_network')
    location = PointField()
    info = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__node_metadata'
        unique_together = (('id', 'sensor_network'),)

    def __str__(self):
        return self.id


class Sensor(Model):
    name = CharField(primary_key=True, max_length=255)
    observed_properties = JSONField(blank=True, null=True)
    info = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__sensor_metadata'

    def __str__(self):
        return self.name


class Feature(Model):
    name = CharField(primary_key=True, max_length=255)
    observed_properties = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__feature_metadata'

    def clean(self):
        validate_feature(self)

    def __str__(self):
        return self.name


class SensorFeatureToNetwork(Model):
    feature = ForeignKey(Feature, DO_NOTHING, db_column='feature')
    network = ForeignKey(Network, DO_NOTHING, db_column='network')

    class Meta:
        db_table = 'sensor__feature_to_network'


class SensorSensorToNode(Model):
    sensor = ForeignKey(Sensor, DO_NOTHING, db_column='sensor')
    network = ForeignKey(Node, DO_NOTHING, db_column='network')
    node = CharField(max_length=255)

    class Meta:
        db_table = 'sensor__sensor_to_node'
