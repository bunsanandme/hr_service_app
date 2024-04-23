from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from datetime import datetime

class User(AbstractUser):
    birth_date = models.DateField(default=datetime.now, blank=True)
    phone_number = PhoneNumberField(blank=True)
    education = models.CharField(blank=True, max_length=128)
    document_scan = models.FileField(blank=True)
    position = models.CharField(blank=True, max_length=64)
    photo = models.ImageField(blank=True)
    start_job_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.position}"