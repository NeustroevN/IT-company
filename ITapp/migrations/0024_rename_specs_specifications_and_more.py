# Generated by Django 5.0.4 on 2024-09-26 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITapp', '0023_rename_solution_solspecs_solution_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Specs',
            new_name='Specifications',
        ),
        migrations.RenameField(
            model_name='benefits',
            old_name='deckription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='purchases',
            old_name='deckription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='solspecs',
            old_name='specs',
            new_name='specification',
        ),
    ]
