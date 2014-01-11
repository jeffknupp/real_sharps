# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PickClass.description'
        db.add_column(u'cappers_pickclass', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


        # Changing field 'PickClass.name'
        db.alter_column(u'cappers_pickclass', 'name', self.gf('django.db.models.fields.CharField')(max_length=250))

    def backwards(self, orm):
        # Deleting field 'PickClass.description'
        db.delete_column(u'cappers_pickclass', 'description')


        # Changing field 'PickClass.name'
        db.alter_column(u'cappers_pickclass', 'name', self.gf('django.db.models.fields.TextField')())

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'cappers.handicapper': {
            'Meta': {'object_name': 'Handicapper', '_ormbases': [u'auth.User']},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'specialty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cappers.Sport']", 'null': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cappers.pick': {
            'Meta': {'object_name': 'Pick', '_ormbases': [u'cappers.UpdateMixin']},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_post'", 'to': u"orm['cappers.Handicapper']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'pick_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cappers.PickClass']", 'null': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            u'updatemixin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cappers.UpdateMixin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cappers.pickclass': {
            'Meta': {'object_name': 'PickClass'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'cappers.pickproduct': {
            'Meta': {'object_name': 'PickProduct', '_ormbases': [u'cappers.Pick', u'cappers.Product']},
            u'pick_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cappers.Pick']", 'unique': 'True', 'primary_key': 'True'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cappers.Product']", 'unique': 'True'})
        },
        u'cappers.pickset': {
            'Meta': {'object_name': 'PickSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'picks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cappers.Pick']", 'symmetrical': 'False'})
        },
        u'cappers.picksetproduct': {
            'Meta': {'object_name': 'PickSetProduct', '_ormbases': [u'cappers.PickSet', u'cappers.Product']},
            u'pickset_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cappers.PickSet']", 'unique': 'True', 'primary_key': 'True'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cappers.Product']", 'unique': 'True'})
        },
        u'cappers.product': {
            'Meta': {'object_name': 'Product'},
            'available_after': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'teaser': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'cappers.purchase': {
            'Meta': {'object_name': 'Purchase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cappers.Product']"}),
            'purchase_id': ('django.db.models.fields.TextField', [], {}),
            'purchased_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'valid_until': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'cappers.sport': {
            'Meta': {'object_name': 'Sport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'cappers.updatemixin': {
            'Meta': {'object_name': 'UpdateMixin'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cappers']