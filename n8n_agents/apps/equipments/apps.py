from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EquipmentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.equipments"
    label = "equipments"
    verbose_name = _("Equipments")