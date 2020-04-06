# Generated by Django 3.0.4 on 2020-04-06 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_auto_20200404_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='recurring',
        ),
        migrations.AddField(
            model_name='event',
            name='infoLink',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='weitere Infos (Link)'),
        ),
    ]
