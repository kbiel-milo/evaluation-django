from django.contrib import admin

from tasks.models import ExternalProject, InternalProject, InternalProjectTask


class InternalProjectTaskInline(admin.TabularInline):
    model = InternalProjectTask
    extra = 1


@admin.register(InternalProject)
class InternalProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "production_cost", "maintanance_cost")
    inlines = [InternalProjectTaskInline]


@admin.register(InternalProjectTask)
class InternalProjectTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "completed")


@admin.register(ExternalProject)
class ExternalProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "client_name")
