from django.contrib import admin

from .models import BloodGroups, Roles

# Register your models here.

admin.site.register(BloodGroups)
admin.site.register(Roles)
