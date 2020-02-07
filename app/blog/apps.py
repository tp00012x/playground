from django.apps import AppConfig
from django.db.models.fields import Field

from .custom_lookups import NotEqual


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        Field.register_lookup(NotEqual)
