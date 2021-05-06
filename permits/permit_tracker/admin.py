from django.contrib import admin
from .models import Permit
# # Register your models here.
@admin.register(Permit)
class PermitAdmin(admin.ModelAdmin):
    list_display = ('name', 'permit_type', 'permit_conditions','site', 'area','issue_date' )