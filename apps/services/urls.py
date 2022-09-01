from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('departments', views.departments, name='departments'),
    path('departments/<slug:slug>/',
         views.doctors_by_department, name='doctors_by_department'),
    path('book-appointment/<int:pk>/', views.book_appointment_view,
         name='book_appointment_view'),
    path('appointments/', views.patient_appointments_list_view,
         name='patient_appointments_list_view'),
]
