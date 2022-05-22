from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class VoprosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'otvetRU.ovetRU.vopros'
    verbose_name = _(u'vopros')
