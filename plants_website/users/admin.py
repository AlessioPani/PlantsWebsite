from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    '''
    Custom admin panel configuration. 
    '''
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']
    list_filter = ['username', 'email', 'is_staff']


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
