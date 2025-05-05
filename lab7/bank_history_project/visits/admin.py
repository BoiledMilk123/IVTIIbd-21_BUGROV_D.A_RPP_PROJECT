from django.contrib import admin
from .models import Client, Employee, Branch, Service, Visit, VisitService

# Inline для VisitService
class VisitServiceInline(admin.TabularInline):
    model = VisitService
    extra = 1
    verbose_name = 'Услуга посещения'
    verbose_name_plural = 'Услуги посещения'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    search_fields = ('full_name', 'email')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('client', 'employee', 'branch', 'visit_date', 'visit_type')
    list_filter = ('visit_type', 'branch', 'visit_date')
    search_fields = ('client__full_name', 'employee__full_name', 'visit_type')
    inlines = [VisitServiceInline]

@admin.register(VisitService)
class VisitServiceAdmin(admin.ModelAdmin):
    list_display = ('visit', 'service')
    search_fields = ('visit__client__full_name', 'service__name')
