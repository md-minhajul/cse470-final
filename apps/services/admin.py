from django.contrib import admin

from .models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'appointmentDate', 'status']
    list_filter = ['status']
    list_editable = ['status']


@admin.register(Ambulence)
class AmbulenceAdmin(admin.ModelAdmin):
    list_display = ['patient', 'phone_num', 'requested_on', 'is_available']
    list_filter = ['is_available']
    list_editable = ['is_available']
