# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Microblog.message'
        db.alter_column('microblog_microblog', 'message', self.gf('django.db.models.fields.CharField')(max_length=160))


    def backwards(self, orm):
        
        # Changing field 'Microblog.message'
        db.alter_column('microblog_microblog', 'message', self.gf('django.db.models.fields.CharField')(max_length=60))


    models = {
        'microblog.microblog': {
            'Meta': {'object_name': 'Microblog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['microblog']
