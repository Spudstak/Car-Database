#Importing django assets
from django.contrib import admin
from .models import CarType, Manufacturer, CarModel
# Register your models here.

#
class CarAdmin(admin.ModelAdmin):
    #fields = ["model_title","model_published","model_info"]

#Setting what models are related to which fieldsets
    fieldsets = [
        ("Title/date", {"fields": ["model_title", "model_published"]}),
        ("URL", {"fields":["model_slug"]}),
        ("Series", {"fields":["car_manufacturer"]}),
        ("Content", {"fields":["model_info"]}),
        ("Image", {"fields":["model_image"]})
        ]

#Registering the manufacturer, cartype, and carmodel
admin.site.register(Manufacturer)
admin.site.register(CarType)

admin.site.register(CarModel, CarAdmin)
