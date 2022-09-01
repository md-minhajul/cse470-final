# Generated by Django 4.0.6 on 2022-08-22 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_doctor_schedule_alter_patient_user'),
        ('services', '0004_appointment_doctor_alter_appointment_patient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientDischargeDetails',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Symptoms and Descriptions'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appointed_patient', to='accounts.patient'),
        ),
    ]
