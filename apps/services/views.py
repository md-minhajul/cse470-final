from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.accounts.models import *
from .models import *
from .forms import *


def home_view(request):
    form = AmbulenceForm()
    if request.method == 'POST':
        form = AmbulenceForm(request.POST)
        if form.is_valid():
            ambulence = form.save(commit=False)
            patient = Patient.objects.get(user=request.user)
            ambulence.patient = patient
            is_avaibale = False
            ambulence.save()
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'services/index.html', context={'form': form})


def departments(request):
    departments = Department.objects.all().order_by('name')
    return render(request, 'services/departments.html', context={'departments': departments})


def doctors_by_department(request, slug=None):
    department = get_object_or_404(Department, slug=slug)
    doctors = Doctor.objects.filter(department=department)
    return render(request, 'services/doctors_by_department.html', {'department': department, 'doctors': doctors})


@login_required(login_url='/account/patient-login')
def book_appointment_view(request, pk=None):
    doctor = Doctor.objects.get(pk=pk)
    appointmentForm = AppointmentForm()
    mydict = {'doctor': doctor, 'appointmentForm': appointmentForm, }

    if request.method == 'POST':
        appointmentForm = AppointmentForm(request.POST)
        if appointmentForm.is_valid():
            appointment = appointmentForm.save(commit=False)
            appointment.doctor = doctor
            patient = Patient.objects.get(user=request.user)
            appointment.patient = patient
            appointment.doctorName = doctor.get_full_name
            appointment.patientName = patient.full_name
            appointment.status = False
            appointment.save()
        # return HttpResponse('Appointment Booked Successfully')
        return HttpResponseRedirect(reverse('services:patient_appointments_list_view'))

    return render(request, 'services/book_appointment.html', context=mydict)


@ login_required(login_url='/account/patient-login')
def patient_appointments_list_view(request):
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient, status=True)
    return render(request, 'services/appointsments_list.html', context={'appointments': appointments})
