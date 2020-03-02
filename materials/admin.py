from django.contrib import admin

from .models import *

class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('house_id', 'item_name', 'date_received', 'quantity', 'item_unit', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('house_id', )
    search_fields = ('item_name', )

admin.site.register(Materials, MaterialsAdmin)
