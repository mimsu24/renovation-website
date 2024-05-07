from django.contrib import admin
from .models import HouseType, FloorMaterial, WallMaterial, BathroomShower, BathroomSink, BathroomSpecialItem, BathroomToilet


admin.site.register(HouseType)
admin.site.register(FloorMaterial)
admin.site.register(WallMaterial)
admin.site.register(BathroomToilet)
admin.site.register(BathroomShower)
admin.site.register(BathroomSink)
admin.site.register(BathroomSpecialItem)

