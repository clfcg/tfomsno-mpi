from django.contrib import admin

from .models import *


class MpiServicesAdmin(admin.ModelAdmin):
    list_display = ("id","service_name", "service_description", "is_active")
    list_display_links = ("id", "service_name")
    list_editable = ("is_active",)


class MpiMethodsAdmin(admin.ModelAdmin):
    list_display = ("id","meth_name", "meth_desc", "mpi_service", "is_active")
    list_display_links = ("id", "meth_name")
    list_editable = ("is_active",)


class NsiSexAdmin(admin.ModelAdmin):
    list_display = ("id", "caption")


class NsiMpiPolisTypeAdmin(admin.ModelAdmin):
    list_display = ("id","caption", "code", "is_active")
    list_display_links = ("id", "caption")
    list_editable = ("is_active",)


class NsiDudlTypeAdmin(admin.ModelAdmin):
    list_display = ("id","caption", "code", "m_ser", "m_num", "is_active")
    list_display_links = ("id", "caption")
    list_editable = ("is_active",)


class MpiShowAdmin(admin.ModelAdmin):
    list_display = ("id","caption", "desc", "is_active")
    list_display_links = ("id", "caption")
    list_editable = ("is_active",)


admin.site.register(MpiServices, MpiServicesAdmin)
admin.site.register(MpiMethods, MpiMethodsAdmin)
admin.site.register(MpiShow, MpiShowAdmin)
admin.site.register(NsiSex, NsiSexAdmin)
admin.site.register(NsiMpiPolisType, NsiMpiPolisTypeAdmin)
admin.site.register(NsiDudlType, NsiDudlTypeAdmin)