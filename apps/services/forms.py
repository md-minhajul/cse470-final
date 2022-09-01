from operator import imod
from socket import fromshare
from django import forms
from .models import *


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['description']


class AmbulenceForm(forms.ModelForm):

    class Meta:
        model = Ambulence
        fields = ['phone_num']
