"""zinnia_threaded_comments"""
__version__ = '0.1'
__license__ = 'BSD License'

__author__ = 'Fantomas42'
__email__ = 'fantomas42@gmail.com'

__url__ = 'https://github.com/Fantomas42/zinnia-threaded-comments'

from zinnia_threaded_comments.models import ThreadedComment
from zinnia_threaded_comments.forms import ThreadedCommentForm


def get_model():
    return ThreadedComment

def get_form():
    return ThreadedCommentForm

