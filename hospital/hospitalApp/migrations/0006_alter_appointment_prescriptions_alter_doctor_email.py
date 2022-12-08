# Generated by Django 4.1.3 on 2022-12-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0005_rename_email_appointment_doctoremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='prescriptions',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
