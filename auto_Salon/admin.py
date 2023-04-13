from django.contrib import admin

# Register your models here
from .models import *

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Stamp)
class StampAdmin(admin.ModelAdmin):
    list_display = ('name', 'descreption')
    

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

@admin.register(Releasedate)
class ReleasedateAdmin(admin.ModelAdmin):
    list_display = ('releasedate',)
    

@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

@admin.register(Typeofcar)
class TypeofcarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

@admin.register(Create)
class CreateAdmin(admin.ModelAdmin):
    list_display = ('car', 'stamp', 'country', 'releasedate', 'price', 'specifications', 'fuel', 'color', 'typeofcar', 'image', )
    



