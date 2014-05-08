# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ClassInstance'
        db.delete_table(u'recomendr_classinstance')

        # Adding model 'CourseInstance'
        db.create_table(u'recomendr_courseinstance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('quarter', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('professor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recomendr.Professor'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recomendr.Course'])),
        ))
        db.send_create_signal(u'recomendr', ['CourseInstance'])


    def backwards(self, orm):
        # Adding model 'ClassInstance'
        db.create_table(u'recomendr_classinstance', (
            ('professor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recomendr.Professor'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recomendr.Course'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('quarter', self.gf('django.db.models.fields.CharField')(max_length=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'recomendr', ['ClassInstance'])

        # Deleting model 'CourseInstance'
        db.delete_table(u'recomendr_courseinstance')


    models = {
        u'recomendr.course': {
            'Meta': {'object_name': 'Course'},
            'course_number': ('django.db.models.fields.IntegerField', [], {}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'recomendr.courseinstance': {
            'Meta': {'object_name': 'CourseInstance'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recomendr.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['recomendr.Professor']"}),
            'quarter': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'recomendr.professor': {
            'Meta': {'object_name': 'Professor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['recomendr']