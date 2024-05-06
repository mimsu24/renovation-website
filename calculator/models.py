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


class MaterialType(models.Model):
    material_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.material_name

class BathroomItem(models.Model):
    bathroom_item = models.CharField(max_length=100)
    bathroom_material = models.ForeignKey(MaterialType, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    add = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f' {self.bathroom_item} {self.bathroom_material} {self.description} {self.add}' 
    
    
"""
class BathroomMaterial(models.Model):
    bathroom_items = models.CharField(max_length=100)
    bathroom_material = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price_per_square_meter = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f" {self.bathroom_items} {self.bathroom_material} ({self.description}) (€{self.price_per_square_meter})" 
"""    
