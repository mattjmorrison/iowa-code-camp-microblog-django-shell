# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Microblog'
        db.create_table('microblog_microblog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('post_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('microblog', ['Microblog'])


    def backwards(self, orm):
        
        # Deleting model 'Microblog'
        db.delete_table('microblog_microblog')


    models = {
        'microblog.microblog': {
            'Meta': {'object_name': 'Microblog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['microblog']
