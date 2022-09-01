# Generated by Django 4.0.6 on 2022-08-22 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_doctor_schedule_alter_patient_user'),
        ('services', '0006_alter_appointment_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulence',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_patient', to='accounts.patient'),
        ),
    ]