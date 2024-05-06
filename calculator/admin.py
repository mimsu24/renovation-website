from django.contrib import admin
from .models import HouseType, FloorMaterial, WallMaterial, MaterialType, BathroomItem
# Register your models here.
admin.site.register(HouseType)
admin.site.register(FloorMaterial)
admin.site.register(WallMaterial)
admin.site.register(BathroomItem)
admin.site.register(MaterialType)
