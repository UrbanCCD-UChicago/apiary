from django.contrib import admin

from .models import Network, Node, Sensor, Feature, Property

admin.site.register(Network)
admin.site.register(Node)
admin.site.register(Sensor)
admin.site.register(Feature)
admin.site.register(Property)
