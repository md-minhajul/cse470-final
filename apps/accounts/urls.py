from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('logout', LogoutView.as_view(
        template_name='services/index.html'), name='logout'),

    # for ADMIN
    path('admin-login/', views.admin_login, name='admin-login'),

    # for PATIENT
    path('patient-signup/', views.patient_signup_view, name='patient-signup'),
    path('patient-login/', views.patient_login, name='patient-login'),



]
