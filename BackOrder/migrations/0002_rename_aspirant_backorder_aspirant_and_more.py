# Generated by Django 5.0.4 on 2024-04-16 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackOrder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backorder',
            old_name='Aspirant',
            new_name='aspirant',
        ),
        migrations.RenameField(
            model_name='backorder',
            old_name='Brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='backorder',
            old_name='Site',
            new_name='site',
        ),
    ]
