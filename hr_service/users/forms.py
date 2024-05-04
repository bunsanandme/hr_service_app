from django.forms import ModelForm
from .models import User
from phonenumber_field.formfields import PhoneNumberField

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username","birth_date", 
                  'education', "phone_number", "position", "start_job_date", 
                  "email", "document_scan", "photo")
        widgets = {
            'name': PhoneNumberField(region="RU")
        }