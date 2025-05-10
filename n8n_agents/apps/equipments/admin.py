from django.contrib import admin
from apps.equipments.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'quantity', 'location', 'created_by', 'last_updated')
    list_filter = ('type', 'location', 'last_updated')
    search_fields = ('name', 'type', 'location')
    readonly_fields = ('last_updated',)
    date_hierarchy = 'last_updated'
    
    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'quantity', 'location')
        }),
        ('Metadata', {
            'fields': ('created_by', 'last_updated'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Automatically set created_by if not already set."""
        if not change and not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
