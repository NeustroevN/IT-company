# Generated by Django 5.0.4 on 2024-04-26 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solspecs',
            old_name='movie',
            new_name='Solution',
        ),
        migrations.RenameField(
            model_name='solspecs',
            old_name='genres',
            new_name='Specs',
        ),
    ]