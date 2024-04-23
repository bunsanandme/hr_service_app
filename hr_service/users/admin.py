from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    exclude = ['last_login', "is_superuser", "is_staff","date_joined", 'user_permissions', "groups"]
    search_fields = ("last_name__startswith", )
    list_display = ("username" ,"last_name", "first_name", "position")