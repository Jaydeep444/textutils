from django.db import models

# Create your models here.
# class Product(models.Model):
#     product_id = models.AutoField
#     product_name = models.CharField(max_length=100)
#     desc = models.CharField(max_length=200)
#     pub_date = models.DateField()

from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 100)

from phone_field import PhoneField
class hospital_detail(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    address = models.CharField(max_length = 100)
    phone = PhoneField(null=False, blank=False, unique=True)

class doctor_detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    phone = PhoneField(null=False, blank=False, unique=True)
    speciality = models.CharField(max_length=50)
    fees = models.IntegerField()

class patient_detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    phone = PhoneField(null=False, blank=False, unique=True)

class contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=200)