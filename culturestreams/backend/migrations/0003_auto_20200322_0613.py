# Generated by Django 3.0.4 on 2020-03-22 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200322_0429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='pub_date',
            new_name='datePublished',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_end_date',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_end_time',
            new_name='endTime',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_organizer',
            new_name='organizer',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_start_date',
            new_name='startDate',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_start_time',
            new_name='startTime',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_tags',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_accessibility',
        ),
        migrations.AddField(
            model_name='event',
            name='availableLiveOnly',
            field=models.BooleanField(default=True),
        ),
    ]
