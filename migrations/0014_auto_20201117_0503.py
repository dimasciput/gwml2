# Generated by Django 2.2.12 on 2020-11-17 05:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0013_view_well_information_uuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constructionstructure',
            options={'ordering': ('top_depth__value',)},
        ),
        migrations.AlterModelOptions(
            name='stratigraphiclog',
            options={'ordering': ('top_depth__value',)},
        ),
        migrations.AddField(
            model_name='well',
            name='time_updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='management',
            name='license',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.License'),
        ),
    ]