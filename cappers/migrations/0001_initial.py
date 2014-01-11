# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UpdateMixin'
        db.create_table(u'cappers_updatemixin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'cappers', ['UpdateMixin'])

        # Adding model 'Sport'
        db.create_table(u'cappers_sport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'cappers', ['Sport'])

        # Adding model 'Handicapper'
        db.create_table(u'cappers_handicapper', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('specialty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cappers.Sport'], null=True)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cappers', ['Handicapper'])

        # Adding model 'PickClass'
        db.create_table(u'cappers_pickclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cappers', ['PickClass'])

        # Adding model 'Pick'
        db.create_table(u'cappers_pick', (
            (u'updatemixin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cappers.UpdateMixin'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='product_post', to=orm['cappers.Handicapper'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pick_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cappers.PickClass'], null=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
        ))
        db.send_create_signal(u'cappers', ['Pick'])

        # Adding model 'PickSet'
        db.create_table(u'cappers_pickset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'cappers', ['PickSet'])

        # Adding M2M table for field picks on 'PickSet'
        m2m_table_name = db.shorten_name(u'cappers_pickset_picks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pickset', models.ForeignKey(orm[u'cappers.pickset'], null=False)),
            ('pick', models.ForeignKey(orm[u'cappers.pick'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pickset_id', 'pick_id'])

        # Adding model 'Product'
        db.create_table(u'cappers_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('available_after', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('teaser', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'cappers', ['Product'])

        # Adding model 'PickProduct'
        db.create_table(u'cappers_pickproduct', (
            (u'product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cappers.Product'], unique=True)),
            (u'pick_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cappers.Pick'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'cappers', ['PickProduct'])

        # Adding model 'PickSetProduct'
        db.create_table(u'cappers_picksetproduct', (
            (u'product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cappers.Product'], unique=True)),
            (u'pickset_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cappers.PickSet'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'cappers', ['PickSetProduct'])

        # Adding model 'Purchase'
        db.create_table(u'cappers_purchase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cappers.Product'])),
            ('purchased_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('purchase_id', self.gf('django.db.models.fields.TextField')()),
            ('valid_until', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'cappers', ['Purchase'])


    def backwards(self, orm):
        # Deleting model 'UpdateMixin'
        db.delete_table(u'cappers_updatemixin')

        # Deleting model 'Sport'
        db.delete_table(u'cappers_sport')

        # Deleting model 'Handicapper'
        db.delete_table(u'cappers_handicapper')

        # Deleting model 'PickClass'
        db.delete_table(u'cappers_pickclass')

        # Deleting model 'Pick'
        db.delete_table(u'cappers_pick')

        # Deleting model 'PickSet'
        db.delete_table(u'cappers_pickset')

        # Removing M2M table for field picks on 'PickSet'
        db.delete_table(db.shorten_name(u'cappers_pickset_picks'))

        # Deleting model 'Product'
        db.delete_table(u'cappers_product')

        # Deleting model 'PickProduct'
        db.delete_table(u'cappers_pickproduct')

        # Deleting model 'PickSetProduct'
        db.delete_table(u'cappers_picksetproduct')

        # Deleting model 'Purchase'
        db.delete_table(u'cappers_purchase')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
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