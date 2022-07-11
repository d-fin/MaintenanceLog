from django.db import models

# Create your models here.
class Brush(models.Model):
    id = models.IntegerField(primary_key=True)
    side = models.CharField(max_length=1)
    setNum = models.IntegerField()
    brushStyle = models.TextField(max_length=30)
    siteCode = models.IntegerField()

class BrushComponent(models.Model):
    id = models.IntegerField(primary_key=True)
    brushID = models.IntegerField()
    motor = models.DateField('%mm/%dd/%yyyy', null=True)
    shaft = models.DateField('%mm/%dd/%yyyy', null=True)
    bearings = models.DateField('%mm/%dd/%yyyy', null=True)
    upperBearings = models.DateField('%mm/%dd/%yyyy', null=True)
    cloth = models.DateField('%mm/%dd/%yyyy', null=True)
    shocks = models.DateField('%mm/%dd/%yyyy', null=True)
    siteCode = models.IntegerField()

class Maintenance(models.Model):
    id = models.IntegerField(primary_key=True)
    component = models.TextField(max_length=100)
    dateReplaced = models.DateField('%mm/%dd/%yyyy', null=True)
    dueDate = models.DateField('%mm/%dd/%yyyy', null=True)
    notes = models.TextField(max_length=1000, null=True)
    siteCode = models.IntegerField() 

class Inventory(models.Model):
    ''' will have two different motors and two different shocks '''
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=50, null=True)
    modelNumber = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(null=False)
