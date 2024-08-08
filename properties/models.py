from django.db import models

# Create your models here.
class PropertyCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True,null=True)
    category = models.ForeignKey(PropertyCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/images/', height_field=None, width_field=None, max_length=None)
    price = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)
    description = models.TextField()
    space = models.IntegerField()
    floor_number = models.IntegerField()
    bathrooms = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    parking = models.PositiveIntegerField()
    #payment = models.CharField(max_length=50)

    def __str__(self):
        return self.name
