# Generated by Django 3.0.6 on 2020-05-28 12:23

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='doctor_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
                ('speciality', models.CharField(max_length=50)),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hospital_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='patient_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(max_length=31, unique=True)),
            ],
        ),
    ]