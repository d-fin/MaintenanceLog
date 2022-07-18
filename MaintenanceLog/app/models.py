from django.db import models
from django.contrib.auth.models import User
from datetime import date 
from dateutil.relativedelta import relativedelta

today = date.today()
defaultFixDay = (today) + relativedelta(months=6)

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User,
        related_name='employee',
        on_delete=models.CASCADE)
    site = models.IntegerField(default=1)
    darkMode = models.BooleanField(default=False)

class Brush(models.Model):
    id = models.IntegerField(primary_key=True)
    side = models.CharField(max_length=1, null=True)
    setNum = models.IntegerField()
    brushStyle = models.TextField(max_length=30, default="Enter a brush style")
    siteCode = models.IntegerField()

class BrushComponent(models.Model):
    id = models.IntegerField(primary_key=True)
    brushID = models.IntegerField()
    motor = models.DateField('%mm/%dd/%yyyy', default=today)
    shaft = models.DateField('%mm/%dd/%yyyy', default=today)
    bearings = models.DateField('%mm/%dd/%yyyy', default=today)
    upperBearings = models.DateField('%mm/%dd/%yyyy', default=today)
    cloth = models.DateField('%mm/%dd/%yyyy', default=today)
    shocks = models.DateField('%mm/%dd/%yyyy', default=today)
    motorDueDate = models.DateField('%mm/%dd/%yyyy', default=defaultFixDay)
    shaftDueDate = models.DateField('%mm/%dd/%yyyy', default=defaultFixDay)
    bearingsDueDate = models.DateField('%mm/%dd/%yyyy', default=defaultFixDay)
    upperBearingsDueDate = models.DateField('%mm/%dd/%yyyy', default=defaultFixDay)
    clothDueDate = models.DateField('%mm/%dd/%yyyy', default=defaultFixDay)
    shocksDueDate = models.DateField('%mm/%dd/%yyyy', default=defaultFixDay)
    siteCode = models.IntegerField()

class Maintenance(models.Model):
    id = models.IntegerField(primary_key=True)
    component = models.TextField(max_length=100)
    dateReplaced = models.DateField('%mm/%dd/%yyyy', default=today)
    dueDate = models.DateField('%mm/%dd/%yyyy', default=defaultFixDay)
    notes = models.TextField(max_length=1000, default="Enter notes here")
    siteCode = models.IntegerField() 

class Inventory(models.Model):
    id = models.IntegerField(primary_key=True)
    partName = models.CharField(max_length=50, default="Enter a part name")
    modelNumber = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(null=False)
    siteCode = models.IntegerField() 
