# Generated by Django 4.0.6 on 2022-08-21 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_doctor_user'),
        ('services', '0003_remove_appointment_doctor_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointed_doctor', to='accounts.doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='accounts.patient'),
        ),
    ]
