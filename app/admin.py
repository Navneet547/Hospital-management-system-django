from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(doctor_model)
admin.site.register(patient_model)
admin.site.register(staff_model)
admin.site.register(medicine_model)