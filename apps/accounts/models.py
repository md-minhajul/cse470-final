from distutils import text_file
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from apps.services.models import Department
from ckeditor.fields import RichTextField


class LocalUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name='E-mail Address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Patient(models.Model):
    user = models.OneToOneField(
        LocalUser, related_name='patient', on_delete=models.CASCADE)
    profile_pic = models.ImageField(verbose_name='Profile Picture', upload_to="images/",
                                    default="images/500_500.png", null=True, blank=True,)
    address = models.CharField(max_length=40)
    phone_num = models.CharField(verbose_name='Phone Number', max_length=11)
    is_active = models.BooleanField(
        verbose_name='Active status', default=True
    )

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return self.user.full_name

    def get_absolute_url(self):
        return reverse("patient_detail", kwargs={"pk": self.pk})


class Doctor(models.Model):
    user = models.OneToOneField(
        LocalUser, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(
        Department, related_name="department", on_delete=models.CASCADE)
    degree = models.TextField(null=False)
    profile_pic = models.ImageField(verbose_name='Profile Picture', upload_to='images/',
                                    default="images/500_500.png", null=True, blank=True,)
    phone_num = models.CharField(verbose_name='Phone Number', max_length=11)
    schedule = RichTextField(
        config_name='minimal',
        verbose_name='Schedule',
        max_length=500,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name='Active status', default=True
    )

    @property
    def get_full_name(self):
        return self.user.first_name+" "+self.user.last_name

    def get_absolute_url(self):
        return reverse("doctor_detail", kwargs={"pk": self.pk})

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return f"{self.user.first_name} ({self.department})"
