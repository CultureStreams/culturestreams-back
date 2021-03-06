# Generated by Django 3.0.4 on 2020-04-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_auto_20200404_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='description',
            field=models.TextField(blank=True, max_length=700, null=True, verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='plattform',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Beschreibung'),
        ),
    ]
