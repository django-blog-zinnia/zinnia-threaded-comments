from __future__ import unicode_literals

from django.db import migrations


def migrate_comments(apps, schema_editor):
    from zinnia_threaded_comments.models import ThreadedComment

    o_comment_klass = apps.get_model(
        'django_comments', 'Comment')
    t_comment_klass = apps.get_model(
        'zinnia-threaded-comments', 'ThreadedComment')

    for old_comment in o_comment_klass.objects.all():
        comment = t_comment_klass()
        comment.comment = old_comment.comment
        comment.content_type = old_comment.content_type
        comment.ip_address = old_comment.ip_address
        comment.is_public = old_comment.is_public
        comment.is_removed = old_comment.is_removed
        comment.object_pk = old_comment.object_pk
        comment.site = old_comment.site
        comment.submit_date = old_comment.submit_date
        comment.user = old_comment.user
        comment.user_email = old_comment.user_email
        comment.user_name = old_comment.user_name
        comment.user_url = old_comment.user_url
        comment.level = 0
        comment.lft = 0
        comment.rght = 0
        comment.tree_id = 0
        comment.save()
    ThreadedComment.tree.rebuild()


def empty(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia-threaded-comments', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            migrate_comments,
            empty
        )
    ]
