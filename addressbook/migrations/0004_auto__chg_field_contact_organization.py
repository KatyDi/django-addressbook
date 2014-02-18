# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Contact.organization'
        db.alter_column(u'addressbook_contact', 'organization', self.gf('django.db.models.fields.CharField')(max_length='100'))

    def backwards(self, orm):

        # Changing field 'Contact.organization'
        db.alter_column(u'addressbook_contact', 'organization', self.gf('django.db.models.fields.CharField')(max_length='50'))

    models = {
        u'addressbook.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'to': u"orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django_localflavor_us.models.USStateField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': "'10'"})
        },
        u'addressbook.contact': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Contact'},
            'blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['addressbook.ContactGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': "'40'", 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'blank': 'True'}),
            'profile_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'qr_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'40'", 'blank': 'True'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'addressbook.contactgroup': {
            'Meta': {'unique_together': "(('user', 'name'),)", 'object_name': 'ContactGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'40'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'addressbook.email': {
            'Meta': {'object_name': 'Email'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emails'", 'to': u"orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"})
        },
        u'addressbook.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phones'", 'to': u"orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"})
        },
        u'addressbook.socialnetwork': {
            'Meta': {'object_name': 'SocialNetwork'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'social_networks'", 'to': u"orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"})
        },
        u'addressbook.website': {
            'Meta': {'object_name': 'Website'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'websites'", 'to': u"orm['addressbook.Contact']"}),
            'contact_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'blank': 'True'}),
            'public_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['addressbook']