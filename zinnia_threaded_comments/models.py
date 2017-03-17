"""Models for zinnia-threaded-comments"""
from django.utils.translation import ugettext_lazy as _

from django_comments.managers import CommentManager
from django_comments.models import Comment

from mptt.managers import TreeManager
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


class ThreadedComment(MPTTModel, Comment):
    """
    Threaded comments with MPTT
    """

    parent = TreeForeignKey(
        'self',
        related_name='children',
        null=True, blank=True,
        verbose_name=_('reply in comment'))

    objects = CommentManager()
    tree = TreeManager()

    class MPTTMeta:
        """
        Comment MPTT's meta informations.
        """
        order_insertion_by = ['submit_date']
