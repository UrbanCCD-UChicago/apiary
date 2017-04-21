from django.contrib.postgres.fields import JSONField
from django.db.models import CharField, ForeignKey, ManyToManyField, Model


class Network(Model):

    name = CharField(max_length=255, unique=True)
    json = JSONField()
    meta = JSONField()


class Node(Model):

    name = CharField(max_length=255, unique=True)
    network = ForeignKey(Network)
    meta = JSONField()


class Sensor(Model):

    name = CharField(max_length=255, unique=True)
    nodes = ManyToManyField(Node)
    meta = JSONField()


class Feature(Model):

    name = CharField(max_length=255, unique=True)
    sensors = ManyToManyField(Sensor)
    meta = JSONField()


class Property(Model):

    name = CharField(max_length=255)
    unit = CharField(max_length=255)
    primitive = CharField(max_length=255)
    features = ForeignKey(Feature)
    meta = JSONField()
