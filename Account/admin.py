from django.contrib import admin
from .models import Truck, Driver, Trip, Incident, Payment

admin.site.register(Truck)
admin.site.register(Driver)
admin.site.register(Trip)
admin.site.register(Incident)
admin.site.register(Payment)

