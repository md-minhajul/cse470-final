from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = LocalUser
        fields = ['email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = LocalUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class PatientUserForm(forms.ModelForm):
    class Meta:
        model = LocalUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['address', 'phone_num', 'profile_pic']
