# Generated by Django 4.0.6 on 2022-08-22 15:19

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_doctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='schedule',
            field=ckeditor.fields.RichTextField(blank=True, max_length=500, null=True, verbose_name='Schedule'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
