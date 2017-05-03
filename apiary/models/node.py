from apiary.models import Network
from apiary.models.sensor import Sensor
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db.models import CharField, ForeignKey, PointField
from django.contrib.gis.db.models import ManyToManyField
from django.contrib.gis.db.models import Model, DO_NOTHING


class Node(Model):
    id = CharField(primary_key=True, max_length=255)
    sensor_network = ForeignKey(Network, DO_NOTHING, db_column='sensor_network')
    sensors = ManyToManyField(Sensor)
    location = PointField()
    info = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__node_metadata'
        unique_together = (('id', 'sensor_network'),)
        managed = False

    def __str__(self):
        return self.id
