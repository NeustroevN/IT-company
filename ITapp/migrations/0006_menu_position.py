# Generated by Django 5.0.4 on 2024-05-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITapp', '0005_alter_solspecs_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='position',
            field=models.PositiveIntegerField(default=1, verbose_name='Позиция'),
        ),
    ]
