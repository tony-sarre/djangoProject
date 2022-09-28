from django.contrib import admin
from django.shortcuts import render

from sac.models import (Alert, AlertList)


class AlertInline(admin.TabularInline):
    model = Alert
    extra = 0


@admin.register(AlertList)
class AlertListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (AlertInline,)
    pass


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'phone', 'due_date', 'Resolue', 'Encours')
    list_filter = ('due_date', 'Resolue', 'Encours')
    search_fields = ('title',)
