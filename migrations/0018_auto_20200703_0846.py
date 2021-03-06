# Generated by Django 2.2.12 on 2020-07-03 08:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0017_merge_20200703_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='GLEarthMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GWUnitVoidProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gw_permeability', models.ManyToManyField(help_text="Refers to intrinsic permeability: a measure of a material's ability to allow fluid flow that is independent of fluid properties, and based on connectivity of pores and size of their openings. This is not hydraulic conductivity.", to='gwml2.Quantity', verbose_name='gwPermeability')),
                ('gw_porosity', models.ManyToManyField(help_text='Relates possibly many types of porosity values to a unit and related void combination.', to='gwml2.GWPorosity', verbose_name='gwPorosity')),
            ],
        ),
        migrations.CreateModel(
            name='GWUnitFluidProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gw_hydraulic_conductivity', models.ManyToManyField(help_text='Hydraulic conductivity measures how easily a fluid can move through the voids in a material.', to='gwml2.Quantity', verbose_name='gwHydraulicConductivity')),
                ('gw_storativity', models.ManyToManyField(help_text='Storativity is the volume of water released from storage per unit decline in hydraulic head in the aquifer, per unit area of the aquifer.', related_name='gw_storativity', to='gwml2.Quantity', verbose_name='gwStorativity')),
                ('gw_transmissivity', models.ManyToManyField(help_text='The rate of groundwater flow laterally through an aquifer, determined by hydraulic conductivity and container thickness.', related_name='gw_transmissivity', to='gwml2.Quantity', verbose_name='gwTransmissivity')),
                ('gw_yield', models.ManyToManyField(help_text='Relates possibly many types of yield values to a unit and fluid body combination.', to='gwml2.GWYield', verbose_name='gwYield')),
            ],
        ),
        migrations.CreateModel(
            name='GWHydrogeoVoid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gw_void_description', models.TextField(blank=True, help_text='General description of the void.', null=True, verbose_name='gwVoidDescription')),
                ('gw_void_shape', django.contrib.gis.db.models.fields.GeometryField(blank=True, help_text='Shape and position of the void.', null=True, srid=4326, verbose_name='gwVoidShape')),
                ('gw_fluid_body_void', models.ForeignKey(blank=True, help_text='Each void contains at most one fluid body, which can have multiple parts that could be disconnected.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.GWFluidBody', verbose_name='gwFluidBodyVoid')),
                ('gw_part_of_void', models.ForeignKey(blank=True, help_text='Relates a void and a fluid body contained by.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.GWHydrogeoVoid', verbose_name='gwPartOfVoid')),
                ('gw_void_host_material', models.ManyToManyField(blank=True, help_text='The material that hosts the void, if specified. Note voids can be hosted by a unit (an aquifer) or its material (e.g. sandstone).', null=True, to='gwml2.GLEarthMaterial', verbose_name='gwVoidHostMaterial')),
                ('gw_void_metadata', models.ManyToManyField(blank=True, help_text='Metadata for the void.', null=True, to='gwml2.GWMetadata', verbose_name='gwVoidMetadata')),
                ('gw_void_type', models.ForeignKey(blank=True, help_text='Type of void e.g. fractured, intergranular, etc.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.PorosityTypeTerm', verbose_name='gwVoidType')),
                ('gw_void_unit', models.ManyToManyField(blank=True, help_text='Relates hydrogeological units with a void hosted by the units.', null=True, to='gwml2.GWHydrogeoUnit', verbose_name='gwVoidUnit')),
                ('gw_void_volume', models.ForeignKey(blank=True, help_text='Volume of the void.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.Quantity', verbose_name='gwVoidVolume')),
            ],
        ),
        migrations.AddField(
            model_name='glearthmaterial',
            name='gw_fluid_property',
            field=models.ForeignKey(blank=True, help_text='The hydraulic conductivity, transmissivity, or storativity of an earth material.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.GWUnitFluidProperty', verbose_name='gwFluidProperty'),
        ),
        migrations.AddField(
            model_name='glearthmaterial',
            name='gw_void_property',
            field=models.ForeignKey(blank=True, help_text='The porosity or permeability of a particular earth material that hosts a void.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gwml2.GWUnitVoidProperty', verbose_name='gwVoidProperty'),
        ),
    ]
