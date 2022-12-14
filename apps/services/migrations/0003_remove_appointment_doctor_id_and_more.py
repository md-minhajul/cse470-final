# Generated by Django 4.0.6 on 2022-08-21 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_doctor_user'),
        ('services', '0002_department_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctor_id',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='appointed_doctor', to='accounts.doctor'),
        ),
    ]
