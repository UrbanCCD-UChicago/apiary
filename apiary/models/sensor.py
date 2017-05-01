from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db.models import CharField, Model


class Sensor(Model):
    name = CharField(primary_key=True, max_length=255)
    observed_properties = JSONField(blank=True, null=True)
    info = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__sensor_metadata'

    def __str__(self):
        return self.name


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
