from collections import defaultdict
from django.contrib.auth.models import User, Group
from rest_framework_json_api.serializers import ModelSerializer
from rest_framework_json_api.serializers import ValidationError
from .models import Network, Node, Sensor, Feature


def validate_sensor(data):
    observed_properties = data['observed_properties']

    features = defaultdict(list)
    for feature in Feature.objects.all():
        for property_dict in feature.observed_properties:
            features[feature.name].append(property_dict["name"])

    for feature_property in list(observed_properties.values()):
        try:
            feat, prop = feature_property.split(".")
        except ValueError:
            msg = "Feature specified without property: {}"
            raise ValidationError(msg.format(feature_property))

        if feat not in features:
            raise ValidationError("Bad feature name: '{}'".format(feat))
        if prop not in features[feat]:
            raise ValidationError("Bad property name: '{}'".format(prop))

    return data


def validate_feature(data):

    json_list = data['observed_properties']
    if type(json_list) != list:
        raise ValidationError("JSON must be enclosed in brackets: [ {...} ]")

    redshift_type_map = {
        "BOOL": "BOOLEAN",
        "INT": "BIGINT",
        "INTEGER": "BIGINT",
        "DOUBLE": "DOUBLE PRECISION",
        "FLOAT": "DOUBLE PRECISION",
        "STRING": "VARCHAR"
    }

    for property_dict in json_list:
        value = property_dict["type"].upper()
        type_aliases = set(redshift_type_map.keys())
        type_standards = set(redshift_type_map.values())

        if value not in type_standards:
            if value not in type_aliases:
                raise ValidationError("Invalid type provided: {}".format(value))
            else:
                property_dict["type"] = redshift_type_map[value]

    return data
