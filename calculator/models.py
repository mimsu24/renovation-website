from django.db import models


# Create your models here.
class HouseType(models.Model):
    type_of_house = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    add = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.type_of_house} | {self.description} | {self.add}"
    

class FloorMaterial(models.Model):
    floor_material = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price_per_square_meter = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.floor_material} ({self.description}) (€{self.price_per_square_meter})" 
    

class WallMaterial(models.Model):
    wall_material = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price_per_square_meter = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.wall_material} ({self.description}) (€{self.price_per_square_meter})" 


class BathroomToilet(models.Model):
    type_of_toilet = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    add = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.type_of_toilet} | {self.description} | {self.add}"

class BathroomShower(models.Model):
    type_of_shower = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    add = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.type_of_shower} | {self.description} | {self.add}"
    
class BathroomSink(models.Model):
    type_of_sink = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    add = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.type_of_sink} | {self.description} | {self.add}"    

class BathroomSpecialItem(models.Model):
    type_of_item = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    add = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.type_of_item} | {self.description} | {self.add}"    