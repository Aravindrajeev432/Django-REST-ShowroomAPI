from django.contrib import admin
from .models import Cars,DisplayCars,Colours,FuelType,GearType,DisplayCarImages, \
    CarParts,UniPartNumbers
# Register your models here.

admin.site.register(Cars)
admin.site.register(DisplayCars)
admin.site.register(Colours)
admin.site.register(GearType)
admin.site.register(FuelType)
admin.site.register(DisplayCarImages)
admin.site.register(CarParts)
admin.site.register(UniPartNumbers)

