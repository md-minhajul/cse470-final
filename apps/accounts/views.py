import io

from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse

from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render, redirect

from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test

from datetime import date
from xhtml2pdf import pisa


from .forms import *
from .models import *
from apps.services.models import *


def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


###############--------------- USER AUTHENTICATION ---------------###############
def admin_login(request):
    if request.method == 'GET':
        return render(request, 'accounts/admin-login.html', {'form': LoginForm()})
    else:
        user = authenticate(
            request, email=request.POST['email'], password=request.POST['password'])
        if user is None:
            error = {'User and Password did not match'}
            return render(request, 'accounts/admin-login.html', {'form': LoginForm(), 'error': error})

        else:
            login(request, user)

            return HttpResponse('Login Success')
            # return redirect('')


def patient_signup_view(request):
    userForm = PatientUserForm()
    patientForm = PatientForm()
    signupforms = {'userForm': userForm, 'patientForm': patientForm}
    if request.method == 'POST':
        userForm = PatientUserForm(request.POST)
        patientForm = PatientForm(request.POST, request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save(commit=False)
            patient.user = user
            patient = patient.save()
            group = Group.objects.get_or_create(name='PATIENT')
            group[0].user_set.add(user)
        return HttpResponseRedirect(reverse('accounts:patient-login'))
    return render(request, 'accounts/patient-signup.html', context=signupforms)


def patient_login(request):
    if request.method == 'GET':
        return render(request, 'accounts/patient-login.html', {'form': LoginForm()})
    else:
        user = authenticate(
            request, email=request.POST['email'],  password=request.POST['password'])
        if user is None:
            error = 'Username and Password did not match'
            return render(request, 'accounts/patient-login.html', {'form': LoginForm(), 'error': error})
        else:
            login(request, user)
            # return HttpResponse('Login Success')
            return redirect('home')
