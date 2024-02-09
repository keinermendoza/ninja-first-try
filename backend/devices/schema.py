from ninja import ModelSchema
from devices.models import Location, Device

class LocationSchema(ModelSchema):
    class Meta:
        model = Location
        fields = ("id", "name")

class DeviceSchema(ModelSchema):
    location: LocationSchema | None = None

    class Meta:
        model = Device
        fields = ("id" ,"name", "slug", "location")