"""Admin for zinnia-threaded-comments"""
from django.contrib import admin
from django.contrib.comments import get_model
from django.contrib.comments.admin import CommentsAdmin
from django.utils.translation import ugettext_lazy as _

from zinnia_threaded_comments.models import ThreadedComment


class ThreadedCommentAdmin(CommentsAdmin):
    """
    Admin class for threaded comments
    """
    fieldsets = ((None,
                  {'fields': ('content_type', 'object_pk', 'site')}),
                 (_('Content'),
                  {'fields': ('user', 'user_name', 'user_email',
                              'user_url', 'parent', 'comment')}),
                 (_('Metadata'),
                  {'fields': ('submit_date', 'ip_address',
                              'is_public', 'is_removed')}))
    list_display = ('name', 'content_type', 'object_pk',
                    'parent', 'ip_address', 'submit_date',
                    'is_public', 'is_removed')
    raw_id_fields = ('user', 'parent')


if get_model() is ThreadedComment:
    admin.site.register(ThreadedComment, ThreadedCommentAdmin)
