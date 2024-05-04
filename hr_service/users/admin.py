from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm

admin.site.unregister(Group)

@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    exclude = ['last_login', "is_superuser", "is_staff","date_joined", 'user_permissions', "groups"]
    search_fields = ("last_name__startswith", )
    list_display = ("username" ,"last_name", "first_name", "position")
    model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user