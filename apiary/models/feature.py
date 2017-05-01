from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db.models import CharField, Model
from django.forms import ValidationError


class Feature(Model):
    name = CharField(primary_key=True, max_length=255)
    observed_properties = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__feature_metadata'

    def clean(self):
        validate_feature(self)

    def __str__(self):
        return self.name


def validate_feature(feature):

    if not feature.observed_properties:
        raise ValidationError("No properties were provided.")

    if not len(feature.observed_properties):
        raise ValidationError("No properties were provided.")

    json_list = feature.observed_properties
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
        property_keys = property_dict.keys()

        if 'type' not in property_keys or 'name' not in property_keys:
            msg = "Improperly formatted property: {} - a property needs both " \
                  "'name' and 'type' keys.".format(property_dict)
            raise ValidationError(msg)
            
        value = property_dict["type"].upper()
        type_aliases = set(redshift_type_map.keys())
        type_standards = set(redshift_type_map.values())

        if value not in type_standards:
            if value not in type_aliases:
                raise ValidationError("Invalid type provided: {}".format(value))
            else:
                property_dict["type"] = redshift_type_map[value]

    return feature
