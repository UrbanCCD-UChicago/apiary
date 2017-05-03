from django.contrib.postgres.fields import JSONField
from django.contrib.gis.db.models import CharField, Model


class Network(Model):
    name = CharField(primary_key=True, max_length=255)
    info = JSONField(blank=True, null=True)

    class Meta:
        db_table = 'sensor__network_metadata'
        managed = False

    def __str__(self):
        return self.name
