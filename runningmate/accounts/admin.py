
# Register your models here.
from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'email', 'school', 'school_id')
admin.site.register(UserProfile, UserProfileAdmin)