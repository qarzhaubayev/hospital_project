# Generated by Django 4.1.3 on 2022-11-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('surname', models.CharField(max_length=200, null=True)),
                ('midname', models.CharField(max_length=200, null=True)),
                ('date_of_birth', models.CharField(max_length=200, null=True)),
                ('iin_number', models.CharField(max_length=200, null=True)),
                ('id_number', models.CharField(max_length=200, null=True)),
                ('department_id', models.CharField(max_length=200, null=True)),
                ('specialization_details_id', models.CharField(max_length=200, null=True)),
                ('experience', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('price_of_appointment', models.CharField(max_length=200, null=True)),
                ('schedule_details', models.CharField(max_length=200, null=True)),
                ('degree_of_education', models.CharField(max_length=200, null=True)),
                ('rating', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('homepage_url', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('surname', models.CharField(max_length=200, null=True)),
                ('midname', models.CharField(max_length=200, null=True)),
                ('date_of_birth', models.CharField(max_length=200, null=True)),
                ('iin_number', models.CharField(max_length=200, null=True)),
                ('id_number', models.CharField(max_length=200, null=True)),
                ('emergancy_contact_number', models.CharField(max_length=200, null=True)),
                ('phone_num', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('marital_status', models.CharField(max_length=200, null=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
