# Generated by Django 4.1.3 on 2022-12-07 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0004_rename_date_appointment_appointmentdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='email',
            new_name='doctoremail',
        ),
    ]
