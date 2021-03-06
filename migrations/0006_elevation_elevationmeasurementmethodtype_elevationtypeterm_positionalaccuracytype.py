# Generated by Django 2.2.12 on 2020-07-02 09:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0005_auto_20200702_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElevationMeasurementMethodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ElevationTypeTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PositionalAccuracyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Elevation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elevation', django.contrib.gis.db.models.fields.PointField(help_text='Numeric value, coordinate reference system (CRS), and unit of measure (UoM) for the elevation.', srid=4326, verbose_name='elevation')),
                ('elevation_accuracy', models.ForeignKey(blank=True, help_text='Description of the accuracy of the elevation measurement.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.PositionalAccuracyType', verbose_name='elevationAccuracy')),
                ('elevation_measurement_method', models.ForeignKey(blank=True, help_text='Description of the accuracy of the elevation measurement.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.ElevationMeasurementMethodType', verbose_name='elevationMeasurementMethod')),
                ('elevation_type', models.ForeignKey(blank=True, help_text='Type of reference elevation, defined as a feature, e.g. Top of Casing, Ground, etc.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.ElevationTypeTerm', verbose_name='elevationType')),
            ],
        ),
    ]
