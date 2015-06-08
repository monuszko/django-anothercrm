from django.contrib import admin

from .models import Company, Relationship, RelationshipType, Person, Trade


class RelationshipInline(admin.TabularInline):
    model = Relationship 
    extra = 2


class CustomerInline(admin.TabularInline):
    model = Relationship
    extra = 2
    verbose_name = 'customer'
    verbose_name_plural = 'customers'

    def get_queryset(self, request):
        qs = super(CustomerInline, self).get_queryset(request)
        return qs.filter(relatype__category='C')


class EmployeeInline(admin.TabularInline):
    model = Relationship
    extra = 2
    verbose_name = 'employee'
    verbose_name_plural = 'employees'

    def get_queryset(self, request):
        qs = super(EmployeeInline, self).get_queryset(request)
        return qs.filter(relatype__category='E')


class RelationshipAdmin(admin.ModelAdmin):
    model = Relationship
    list_display = ('person', 'relatype', 'company')


class CompanyAdmin(admin.ModelAdmin):
    inlines = (EmployeeInline, CustomerInline,)
    list_display = ('name', 'get_trades')
    #TODO: Find a way to remove duplicates when clicking on trades


class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'modification_date')
    inlines = (RelationshipInline,)



admin.site.register(Company, CompanyAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(RelationshipType)
admin.site.register(Trade)
