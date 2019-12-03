from django.contrib import admin
from django.contrib.auth.models import User
from . import models

admin.site.register(models.Profile)
# admin.site.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username','email','create_date','state']