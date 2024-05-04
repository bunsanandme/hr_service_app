from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from datetime import datetime
from django.urls import reverse 

class User(AbstractUser):
    first_name=models.CharField(blank=False, max_length=128)
    last_name=models.CharField(blank=False, max_length=128)
    birth_date = models.DateField(default=datetime.now, blank=True)
    phone_number = PhoneNumberField(blank=True)
    education = models.CharField(blank=True, max_length=128)
    document_scan = models.FileField(blank=True)
    position = models.CharField(blank=True, max_length=64)
    photo = models.ImageField(blank=True)
    start_job_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.position}"
    
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
    
    def get_formatted_phone_number(self):
        return f"{str(self.phone_number)[:2]}({str(self.phone_number)[2:5]})" + \
        f"{str(self.phone_number)[5:8]}-{str(self.phone_number)[8:10]}-{str(self.phone_number)[10:12]}"