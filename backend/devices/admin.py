from django.contrib import admin
from devices.models import Location, Device

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass
