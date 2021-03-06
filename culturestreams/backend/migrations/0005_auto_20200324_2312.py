# Generated by Django 3.0.4 on 2020-03-24 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200324_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Category'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Category'),
        ),
        migrations.AddField(
            model_name='plattform',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Category'),
        ),
    ]
