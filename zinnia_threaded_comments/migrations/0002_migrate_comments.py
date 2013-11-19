"""Convert comments to threadedcomments"""
from south.v2 import DataMigration
from zinnia_threaded_comments.models import ThreadedComment


class Migration(DataMigration):

    def forwards(self, orm):
        for old_comment in orm['comments.comment'].objects.all():
            comment = orm['zinnia_threaded_comments.threadedcomment']()
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

    def backwards(self, orm):
        orm['zinnia_threaded_comments.threadedcomment'].objects.delete()

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField',
                   [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField',
                     [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField',
                            [], {'to': "orm['auth.Permission']",
                                 'symmetrical': 'False',
                                 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', "
                     "'content_type__model', 'codename')",
                     'unique_together': "(('content_type', 'codename'),)",
                     'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField',
                         [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey',
                             [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField',
                   [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField',
                     [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField',
                            [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField',
                      [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField',
                           [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField',
                       [], {'to': "orm['auth.Group']",
                            'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField',
                   [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField',
                          [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField',
                         [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField',
                             [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField',
                           [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField',
                          [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField',
                         [], {'max_length': '128'}),
            'user_permissions': (
                'django.db.models.fields.related.ManyToManyField',
                [], {'to': "orm['auth.Permission']",
                     'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField',
                         [], {'unique': 'True', 'max_length': '30'})
        },
        'comments.comment': {
            'Meta': {'ordering': "('submit_date',)",
                     'object_name': 'Comment',
                     'db_table': "'django_comments'"},
            'comment': ('django.db.models.fields.TextField',
                        [], {'max_length': '3000'}),
            'content_type': ('django.db.models.fields.related.ForeignKey',
                             [],
                             {'related_name': "'content_type_set_for_comment'",
                              'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField',
                   [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField',
                           [], {'max_length': '15', 'null': 'True',
                                'blank': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField',
                          [], {'default': 'True'}),
            'is_removed': ('django.db.models.fields.BooleanField',
                           [], {'default': 'False'}),
            'object_pk': ('django.db.models.fields.TextField',
                          [], {}),
            'site': ('django.db.models.fields.related.ForeignKey',
                     [], {'to': "orm['sites.Site']"}),
            'submit_date': ('django.db.models.fields.DateTimeField',
                            [], {'default': 'None'}),
            'user': ('django.db.models.fields.related.ForeignKey',
                     [], {'blank': 'True',
                          'related_name': "'comment_comments'",
                          'null': 'True', 'to': "orm['auth.User']"}),
            'user_email': ('django.db.models.fields.EmailField',
                           [], {'max_length': '75', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField',
                          [], {'max_length': '50', 'blank': 'True'}),
            'user_url': ('django.db.models.fields.URLField',
                         [], {'max_length': '200', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)",
                     'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType',
                     'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField',
                          [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField',
                   [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField',
                      [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField',
                     [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)",
                     'object_name': 'Site',
                     'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField',
                       [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField',
                   [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField',
                     [], {'max_length': '50'})
        },
        'zinnia_threaded_comments.threadedcomment': {
            'Meta': {'object_name': 'ThreadedComment',
                     '_ormbases': ['comments.Comment']},
            'comment_ptr': ('django.db.models.fields.related.OneToOneField',
                            [], {'to': "orm['comments.Comment']",
                                 'unique': 'True', 'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField',
                      [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField',
                    [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey',
                       [], {'blank': 'True',
                            'related_name': "'children'",
                            'null': 'True',
                            'to': "orm['zinnia_threaded_comments."
                            "ThreadedComment']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField',
                     [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField',
                        [], {'db_index': 'True'})
        }
    }

    complete_apps = ['zinnia_threaded_comments']
    symmetrical = True
