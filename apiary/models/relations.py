from django.contrib.gis.db.models import CASCADE
from django.contrib.gis.db.models import CharField, ForeignKey, Model

from apiary.models import Network, Node, Feature, Sensor


class SensorFeatureToNetwork(Model):
    feature = ForeignKey(Feature, on_delete=CASCADE, db_column='feature')
    network = ForeignKey(Network, on_delete=CASCADE, db_column='network')

    class Meta:
        db_table = 'sensor__feature_to_network'


class SensorSensorToNode(Model):
    sensor = ForeignKey(Sensor, on_delete=CASCADE, db_column='sensor', primary_key=True)
    network = ForeignKey(Network, on_delete=CASCADE, db_column='network', primary_key=True)
    node = ForeignKey(Node, on_delete=CASCADE, db_column='node', primary_key=True)

    class Meta:
        db_table = 'sensor__sensor_to_node'
        # unique_together = (('sensor', 'network', 'node'))
