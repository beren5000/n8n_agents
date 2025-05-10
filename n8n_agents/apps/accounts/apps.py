from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):
    name = 'apps.accounts'
    label = 'accounts'
    verbose_name = _("Authentication and Authorization")