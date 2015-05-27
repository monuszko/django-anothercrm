from django.contrib import admin

from .models import Company, Relationship, RelationshipType, Person


class RelationshipInline(admin.TabularInline):
    model = Relationship 
    extra = 2


class RelationshipAdmin(admin.ModelAdmin):
    model = Relationship
    list_display = ('person', 'relatype', 'company')


class CompanyAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)


class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'modification_date')



admin.site.register(Company, CompanyAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(RelationshipType)
