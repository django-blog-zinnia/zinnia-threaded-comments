"""zinnia_threaded_comments"""
default_app_config = (
    'zinnia_threaded_comments.apps.ZinniaThreadedCommentsConfig'
)


def get_model():
    from zinnia_threaded_comments.models import ThreadedComment
    return ThreadedComment


def get_form():
    from zinnia_threaded_comments.forms import ThreadedCommentForm
    return ThreadedCommentForm
