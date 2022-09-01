from datetime import datetime
from django.db import models
from django.forms import CharField
from django.urls import reverse

# from apps.accounts.models import Patient, Doctor


class Department(models.Model):
    name = models.CharField(verbose_name='Department Name', max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})


class Appointment(models.Model):
    patient = models.ForeignKey(
        'accounts.Patient', related_name="appointed_patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        'accounts.Doctor', related_name="appointed_doctor", on_delete=models.CASCADE, null=True, blank=True)
    patient_name = models.CharField(max_length=40, null=True)
    doctor_name = models.CharField(max_length=40, null=True)
    appointmentDate = models.DateField(auto_now=True)
    description = models.TextField(
        verbose_name="Symptoms and Descriptions", max_length=500)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.user.full_name

    def get_absolute_url(self):
        return reverse("Appointment_detail", kwargs={"pk": self.pk})


class Ambulence(models.Model):
    phone_num = models.CharField(verbose_name='Phone Number', max_length=11)
    patient = models.ForeignKey(
        'accounts.Patient', related_name="requested_patient", on_delete=models.CASCADE)
    requested_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient.phone_num)
