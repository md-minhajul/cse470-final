from django.contrib import admin

from .models import *


class DoctorInline(admin.TabularInline):
    model = Doctor


@admin.register(LocalUser)
class LocalUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    inlines = [DoctorInline]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'department', 'degree',
                    'phone_num', 'schedule', 'is_active']
    list_editable = ['is_active']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone_num', 'address', 'is_active']
    list_editable = ['is_active']
