"""zinnia_threaded_comments"""
from zinnia_threaded_comments.forms import ThreadedCommentForm
from zinnia_threaded_comments.models import ThreadedComment


def get_model():
    return ThreadedComment


def get_form():
    return ThreadedCommentForm
