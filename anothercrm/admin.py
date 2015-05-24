from django.contrib import admin

from .models import Company, Employee


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 2


class CompanyAdmin(admin.ModelAdmin):
    inlines = (EmployeeInline,)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee)
