# Generated by Django 2.2.12 on 2021-01-04 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwml2', '0041_auto_20201231_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadsession',
            name='downloadable',
            field=models.BooleanField(default=True, help_text='indicate that well can be downloaded'),
        ),
    ]