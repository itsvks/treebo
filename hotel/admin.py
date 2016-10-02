from django.contrib import admin
from import_export.admin import ImportExportMixin

from hotel.models import Deals
from hotel.resources import DealsResource


class DealsAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DealsResource
    list_display = ('id', 'name', 'rating', 'location', 'actual_price', 'discount')

admin.site.register(Deals, DealsAdmin)