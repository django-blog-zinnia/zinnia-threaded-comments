"""zinnia_threaded_comments"""
from zinnia_threaded_comments.models import ThreadedComment
from zinnia_threaded_comments.forms import ThreadedCommentForm


def get_model():
    return ThreadedComment


def get_form():
    return ThreadedCommentForm
