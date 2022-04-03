from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin


# admin.site.register(User)


class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('username', 'roll_number', 'school_name', 'campus_name', 'readable_password')

admin.site.register(User, UserAdmin)