# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Professor'
        db.create_table(u'recomendr_professor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'recomendr', ['Professor'])

        # Adding field 'Class.professor'
        db.add_column(u'recomendr_class', 'professor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['recomendr.Professor']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Professor'
        db.delete_table(u'recomendr_professor')

        # Deleting field 'Class.professor'
        db.delete_column(u'recomendr_class', 'professor_id')


    models = {
        u'recomendr.class': {
            'Meta': {'object_name': 'Class'},
            'course_number': ('django.db.models.fields.IntegerField', [], {}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recomendr.Professor']"}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'recomendr.professor': {
            'Meta': {'object_name': 'Professor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['recomendr']