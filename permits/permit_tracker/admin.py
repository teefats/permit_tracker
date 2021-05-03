from django.contrib import admin
from .models import Permit
# # Register your models here.
@admin.register(Permit)
class PermitAdmin(admin.ModelAdmin):
    list_display = ['name', 'permit_type', 'permit_conditions', 'permit_authority', 'issue_date','expiration_date']
    date_hierarchy ='issue_date'
    