# Generated by Django 4.0.6 on 2022-08-22 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_doctor_schedule_alter_patient_user'),
        ('services', '0005_delete_patientdischargedetails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointed_doctor', to='accounts.doctor'),
        ),
    ]
