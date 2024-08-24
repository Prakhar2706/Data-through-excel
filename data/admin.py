from django.contrib import admin
from .models import Lead, University

# Register your models here.

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'university_name', 'state_field', 'city_field')
    search_fields = ('university_name', 'state_field', 'city_field')
    list_filter = ('university_name',)
    ordering = ('id',)

class LeadAdmin(admin.ModelAdmin):
    list_display = ('id','name','university', 'state', 'city', 'program', 'course', 'phone')
    readonly_fields = ('created_at',)
    search_fields = ('id', 'name', 'university', 'state', 'city')
    ordering = ('id',)

admin.site.register(Lead, LeadAdmin)
admin.site.register(University, UniversityAdmin)