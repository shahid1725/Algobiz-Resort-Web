from django.db import models
from location_field.models.plain import PlainLocationField


class Product(models.Model):
    name=models.CharField(max_length=120)
    price=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to="productmages",null=True)
    city = models.CharField(max_length=255,null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7,null=True)

    def __str__(self):
        return self.name


