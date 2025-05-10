from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Equipment(models.Model):
    """Model for warehouse equipment inventory."""
    
    name = models.CharField(_('name'), max_length=255)
    type = models.CharField(_('type'), max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='equipments',
        verbose_name=_('created by')
    )
    quantity = models.PositiveIntegerField(_('quantity'), default=0)
    location = models.CharField(_('location'), max_length=255)
    last_updated = models.DateTimeField(_('last updated'), default=timezone.now)
    
    class Meta:
        db_table = "equipments"
        verbose_name = _("Equipment")
        verbose_name_plural = _("Equipment")
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.type}) - {self.quantity} units at {self.location}"
    
    def update_quantity(self, new_quantity):
        """Update the quantity and last_updated fields."""
        self.quantity = new_quantity
        self.last_updated = timezone.now()
        self.save()
