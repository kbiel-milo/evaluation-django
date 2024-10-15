from tasks.models import ExternalProject, InternalProject
from django.contrib import admin


@admin.register(InternalProject)
class InternalProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "production_cost", "maintanance_cost")


@admin.register(ExternalProject)
class ExternalProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "client_name")
