"""Models for zinnia-threaded-comments"""
from django.utils.translation import ugettext_lazy as _

from django_comments.models import Comment
from django_comments.managers import CommentManager

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
from mptt.managers import TreeManager


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
