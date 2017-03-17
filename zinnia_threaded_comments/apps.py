"""Apps for zinnia-threaded-comments"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ZinniaThreadedCommentsConfig(AppConfig):
    """
    Config for Zinnia Threaded Comments application.
    """
    name = 'zinnia_threaded_comments'
    label = 'zinnia-threaded-comments'
    verbose_name = _('Comments')
