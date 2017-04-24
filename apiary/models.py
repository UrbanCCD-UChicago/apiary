from django.contrib.postgres.fields import JSONField
from django.db.models import CharField, ForeignKey, ManyToManyField, Model


class Network(Model):

    name = CharField(max_length=255, unique=True)
    json = JSONField(null=True)
    meta = JSONField(null=True)


class Node(Model):

    name = CharField(max_length=255, unique=True)
    network = ForeignKey(Network)
    meta = JSONField(null=True)


class Sensor(Model):

    name = CharField(max_length=255, unique=True)
    nodes = ManyToManyField(Node)
    meta = JSONField(null=True)


class Feature(Model):

    name = CharField(max_length=255, unique=True)
    sensors = ManyToManyField(Sensor)
    meta = JSONField(null=True)


class Property(Model):

    name = CharField(max_length=255)
    unit = CharField(max_length=255)
    primitive = CharField(max_length=255)
    features = ForeignKey(Feature)
    meta = JSONField(null=True)
