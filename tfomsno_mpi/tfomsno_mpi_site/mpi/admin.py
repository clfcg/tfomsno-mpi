from django.contrib import admin

from .models import MpiServices


class MpiServicesAdmin(admin.ModelAdmin):
    list_display = ("id","service_name", "service_description", "is_active")
    list_display_links = ("id", "service_name")
    list_editable = ("is_active",)


admin.site.register(MpiServices, MpiServicesAdmin)