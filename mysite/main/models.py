#Importing django assets
from django.db import models
from datetime import datetime

#Creating the cartype and allowing the superuser to create data for the database
class CarType(models.Model):
    car_category = models.CharField(max_length=200)
    car_summary = models.CharField(max_length=200)
    car_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "CarType"

    def __str__(self):
        return self.car_category

#Creating the manufacturer and allowing the superuser to create data for the database
class Manufacturer(models.Model):
    car_manufacturer = models.CharField(max_length=200)
    car_category = models.ForeignKey(CarType, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    manufacturer_summary = models.TextField()

    class Meta:
        verbose_name_plural = "Manufacturer"

    def __str__(self):
        return self.car_manufacturer

#Creating the carmodel and allowing the superuser to create data for the database
class CarModel(models.Model):
    model_title = models.CharField(max_length=200)
    model_info = models.TextField()
    model_published = models.DateTimeField('last edited', default=datetime.now)

    car_manufacturer = models.ForeignKey(Manufacturer, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    model_slug = models.CharField(max_length=200, default=1)
    model_image = models.ImageField(upload_to='images',blank=True)

    class Meta:
        verbose_name_plural = "CarModel"
    
    def __str__(self):
        return self.model_title
