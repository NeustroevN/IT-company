# Generated by Django 5.0.4 on 2024-05-25 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITapp', '0020_solution_solution_specification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solution',
            old_name='solution_specification',
            new_name='solution_specifications',
        ),
    ]
