from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StoresConfig(AppConfig):
    name = "e_commerce.stores"
    verbose_name = _("Stores")
