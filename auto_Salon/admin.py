from django.contrib import admin

# Register your models here
from .models import *

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    