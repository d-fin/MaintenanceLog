from django.contrib import admin
from .models import Brush, BrushComponent, HydraulicHoses, Maintenance, Inventory


# Register your models here.
admin.site.register(Brush)
admin.site.register(BrushComponent)
admin.site.register(Maintenance)
admin.site.register(Inventory)
admin.site.register(HydraulicHoses)