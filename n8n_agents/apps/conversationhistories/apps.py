from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ConversationhistoriesConfig(AppConfig):
    """Django AppConfig for the conversation histories module."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.conversationhistories"
    label = "conversationhistories"
    verbose_name = _("Conversation Histories")
