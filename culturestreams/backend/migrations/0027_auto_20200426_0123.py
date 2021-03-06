# Generated by Django 3.0.4 on 2020-04-25 23:23

import autoslug.fields
import backend.helpers
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('backend', '0026_auto_20200409_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name', unique_with=('name',))),
                ('is_artist', models.BooleanField(default=False)),
                ('is_host', models.BooleanField(default=False)),
                ('is_location', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True, max_length=250, null=True, verbose_name='Webseite')),
                ('description', models.TextField(blank=True, max_length=700, null=True, verbose_name='Beschreibung')),
                ('image', models.URLField(blank=True, max_length=250, null=True, verbose_name='Bild')),
                ('datePublished', backend.helpers.CustomDateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Category')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='member',
            field=models.ManyToManyField(blank=True, null=True, to='backend.Member'),
        ),
    ]
