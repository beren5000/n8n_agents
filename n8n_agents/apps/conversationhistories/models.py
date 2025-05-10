from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from apps.accounts.models import User


class ConversationHistory(models.Model):
    """
    Model for storing conversation history between users and the AI agent.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='conversations',
        verbose_name=_('user')
    )
    timestamp = models.DateTimeField(_('timestamp'), default=timezone.now)
    query = models.TextField(_('query'))
    response = models.TextField(_('response'))

    class Meta:
        db_table = "conversation_histories"
        verbose_name = _("Conversation History")
        verbose_name_plural = _("Conversation Histories")
        ordering = ['-timestamp']

    def __str__(self):
        return f"Conversation with {self.user.email} at {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
