from django.contrib import admin
from .models import Incidence, County
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('title','date_reported','location')
    search_fields = ('title',)
    filter_fields = ('title','date_reported')

class CountyAdmin(LeafletGeoAdmin):
    list_display = ('counties','cty_code', 'codes')
    search_fields = ('counties',)
    filter_fields = ('counties','cty_code')

admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(County, CountyAdmin)