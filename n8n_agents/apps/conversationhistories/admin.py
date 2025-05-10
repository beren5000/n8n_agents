from django.contrib import admin
from apps.conversationhistories.models import ConversationHistory


@admin.register(ConversationHistory)
class ConversationHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'truncated_query', 'truncated_response')
    list_filter = ('timestamp', 'user')
    search_fields = ('query', 'response', 'user__email')
    date_hierarchy = 'timestamp'
    readonly_fields = ('timestamp',)
    
    def truncated_query(self, obj):
        """Return truncated query text for display in the list view."""
        return obj.query[:50] + '...' if len(obj.query) > 50 else obj.query
    truncated_query.short_description = 'Query'
    
    def truncated_response(self, obj):
        """Return truncated response text for display in the list view."""
        return obj.response[:50] + '...' if len(obj.response) > 50 else obj.response
    truncated_response.short_description = 'Response'
    
    fieldsets = (
        (None, {
            'fields': ('user', 'timestamp')
        }),
        ('Conversation', {
            'fields': ('query', 'response'),
            'classes': ('wide',)
        }),
    )
