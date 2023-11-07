from django.contrib import admin
from .models import Online_Appointment, Service_Category

# Register your models here.
admin.site.register(Online_Appointment)
admin.site.register(Service_Category)