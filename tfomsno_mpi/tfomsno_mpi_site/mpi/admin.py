from django.contrib import admin

from .models import MpiServices, MpiMethods


class MpiServicesAdmin(admin.ModelAdmin):
    list_display = ("id","service_name", "service_description", "is_active")
    list_display_links = ("id", "service_name")
    list_editable = ("is_active",)


class MpiMethodsAdmin(admin.ModelAdmin):
    list_display = ("id","meth_name", "meth_desc", "mpi_service", "is_active")
    list_display_links = ("id", "meth_name")
    list_editable = ("is_active",)


admin.site.register(MpiServices, MpiServicesAdmin)
admin.site.register(MpiMethods, MpiMethodsAdmin)