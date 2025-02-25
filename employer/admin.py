from django.contrib import admin
from . import models

# Register your models here.

class IndustryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('address',), }
    
admin.site.register(models.Industry, IndustryAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Employer)
admin.site.register(models.Job)
