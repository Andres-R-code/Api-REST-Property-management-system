from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserCustom


# Register your models here.
admin.site.register(UserCustom, UserAdmin) 
