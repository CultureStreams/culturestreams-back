# Generated by Django 3.0.4 on 2020-03-22 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=200)),
                ('event_organizer', models.CharField(max_length=200)),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
                ('event_start_time', models.TimeField()),
                ('event_end_time', models.TimeField()),
                ('event_accessibility', models.CharField(choices=[('live', 'live only'), ('permanent', 'permanent')], max_length=25)),
                ('event_link', models.URLField(max_length=250)),
                ('event_description', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('event_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Category')),
                ('event_tags', models.ManyToManyField(blank=True, to='backend.Tag')),
            ],
        ),
    ]
