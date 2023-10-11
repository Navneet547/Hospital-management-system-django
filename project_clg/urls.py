
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',landing.as_view(),name="landing" ),
    path('admin-hos/',admin_hos.as_view(),name="admin_hos" ),
    path('userform/',userformview.as_view(),name="userform"),
    path('homepage/',Homepageview.as_view(),name="homepage" ),
    path('doctor_page/',doctor_detail.as_view(),name="doctor_url" ),
    path('patient_page/',patient_page.as_view(),name="patient_url" ),
    path('staff_page/',staff_page.as_view(),name="staff_url" ),
    path('medicine_page/',medicine_page.as_view(),name="medicine_url"),
]
