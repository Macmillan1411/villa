from django.db import models

# Create your models here.
class PropertyCategory(models.Model):
    name = models.CharField(max_length=100)


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True,null=True)
    category = models.ForeignKey(PropertyCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    description = models.TextField()
    space = models.IntegerField()
    floor_number = models.IntegerField()
    bathrooms = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    parking = models.PositiveIntegerField()
    #payment = models.CharField(max_length=50)
