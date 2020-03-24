# Generated by Django 3.0.4 on 2020-03-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, to='backend.Tag'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='backend.Tag'),
        ),
        migrations.AlterField(
            model_name='plattform',
            name='tags',
            field=models.ManyToManyField(blank=True, to='backend.Tag'),
        ),
    ]