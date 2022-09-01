# Generated by Django 4.0.6 on 2022-08-20 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDischargeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.PositiveIntegerField(null=True)),
                ('patient_name', models.CharField(max_length=40)),
                ('assigned_doctor_name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('symptoms', models.CharField(max_length=100, null=True)),
                ('admit_date', models.DateField()),
                ('release_date', models.DateField()),
                ('day_spent', models.PositiveIntegerField()),
                ('room_charge', models.PositiveIntegerField()),
                ('medicine_cost', models.PositiveIntegerField()),
                ('doctor_fee', models.PositiveIntegerField()),
                ('other_charge', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.PositiveIntegerField(null=True)),
                ('patient_name', models.CharField(max_length=40, null=True)),
                ('doctor_name', models.CharField(max_length=40, null=True)),
                ('appointmentDate', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='accounts.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Ambulence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.CharField(max_length=11, verbose_name='Phone Number')),
                ('requested_on', models.DateTimeField(auto_now=True)),
                ('is_available', models.BooleanField(default=False)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='requested_patient', to='accounts.patient')),
            ],
        ),
    ]