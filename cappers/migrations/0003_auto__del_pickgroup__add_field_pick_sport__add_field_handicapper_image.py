# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PickGroup'
        db.delete_table(u'cappers_pickgroup')

        # Removing M2M table for field picks on 'PickGroup'
        db.delete_table(db.shorten_name(u'cappers_pickgroup_picks'))

        # Adding field 'Pick.sport'
        db.add_column(u'cappers_pick', 'sport',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['cappers.Sport']),
                      keep_default=False)

        # Adding field 'Handicapper.image'
        db.add_column(u'cappers_handicapper', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Purchase.picks'
        db.alter_column(u'cappers_purchase', 'picks_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cappers.Pick']))

    def backwards(self, orm):
        # Adding model 'PickGroup'
        db.create_table(u'cappers_pickgroup', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'cappers', ['PickGroup'])

        # Adding M2M table for field picks on 'PickGroup'
        m2m_table_name = db.shorten_name(u'cappers_pickgroup_picks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pickgroup', models.ForeignKey(orm[u'cappers.pickgroup'], null=False)),
            ('pick', models.ForeignKey(orm[u'cappers.pick'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pickgroup_id', 'pick_id'])

        # Deleting field 'Pick.sport'
        db.delete_column(u'cappers_pick', 'sport_id')

        # Deleting field 'Handicapper.image'
        db.delete_column(u'cappers_handicapper', 'image')


        # Changing field 'Purchase.picks'
        db.alter_column(u'cappers_purchase', 'picks_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cappers.PickGroup']))

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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'specialty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cappers.Sport']", 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cappers.pick': {
            'Meta': {'object_name': 'Pick'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_post'", 'to': u"orm['cappers.Handicapper']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'for_sale_after': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'pick_text': ('django.db.models.fields.TextField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cappers.Sport']"}),
            'teaser': ('django.db.models.fields.TextField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'cappers.purchase': {
            'Meta': {'object_name': 'Purchase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picks': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cappers.Pick']"}),
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cappers']