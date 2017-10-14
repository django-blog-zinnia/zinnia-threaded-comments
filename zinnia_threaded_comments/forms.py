"""Forms for zinnia-threaded-comments"""
from django import forms

from django_comments.forms import CommentForm

from zinnia_threaded_comments.models import ThreadedComment


class ThreadedCommentForm(CommentForm):
    """
    Threaded comment form
    """
    parent = forms.ModelChoiceField(
        queryset=ThreadedComment.objects.all(),
        widget=forms.HiddenInput(),
        required=False)

    def get_comment_model(self):
        return ThreadedComment

    def get_comment_create_data(self, *args, **kwargs):
        data = super(ThreadedCommentForm, self).get_comment_create_data( *args, **kwargs)
        data['parent'] = self.cleaned_data['parent']
        return data

