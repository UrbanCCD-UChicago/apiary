from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db.models import CharField, ForeignKey, ManyToManyField
from django.contrib.gis.db.models import PointField, Model


class Network(Model):

    name = CharField(max_length=255, unique=True)
    json = JSONField()
    meta = JSONField()

    def __str__(self):
        return self.name


class Node(Model):

    name = CharField(max_length=255, unique=True)
    location = PointField(null=True)
    network = ForeignKey(Network)
    meta = JSONField()

    def __str__(self):
        return self.name


class Sensor(Model):

    name = CharField(max_length=255, unique=True)
    nodes = ManyToManyField(Node)
    meta = JSONField()

    def __str__(self):
        return self.name


class Feature(Model):

    name = CharField(max_length=255, unique=True)
    sensors = ManyToManyField(Sensor)
    meta = JSONField()

    def __str__(self):
        return self.name


class Property(Model):

    name = CharField(max_length=255)
    unit = CharField(max_length=255)
    primitive = CharField(max_length=255)
    features = ForeignKey(Feature)
    meta = JSONField()

    def __str__(self):
        return self.name
