from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin
from import_export import resources

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('username', 'roll_number', 'school_name', 'campus_name', 'readable_password')
        export_order = ['username', 'roll_number', 'school_name', 'campus_name', 'readable_password']
class UserAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('username', 'roll_number', 'school_name', 'campus_name', 'readable_password')
    resource_class = UserResource
admin.site.register(User, UserAdmin)