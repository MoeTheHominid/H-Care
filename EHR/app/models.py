from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Patient(models.Model) :
    pass

class Doctor(models.Model) :
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    birthday = models.DateField()
    speciality = models.CharField(max_length=50)
    email = models.EmailField()

class appointment(models.Model) :
    date = models.DateField()
    reason = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    duration = models.DurationField()
    sort_order = models.IntegerField()

class medication():
    pass