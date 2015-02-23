from django.contrib import admin

from gps.models import GpsNode, GpsNodeMetrics

# Register your models here.
class MetricsInline(admin.TabularInline):
    model = GpsNodeMetrics
    extra = 1

class GpsAdmin(admin.ModelAdmin):
    list_display = ('user', 'ident', 'last_active', 'recently_active')
    list_filter = ['ident']
    search_fields = ['ident']
    fieldsets = [
        (None, {'fields': ['ident', 'user']}),
        ('Last Active', {'fields': ['last_active']}),
    ]
    inlines = [MetricsInline]

admin.site.register(GpsNode, GpsAdmin)
