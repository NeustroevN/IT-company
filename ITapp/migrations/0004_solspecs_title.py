# Generated by Django 5.0.4 on 2024-04-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITapp', '0003_remove_solspecs_specs_solspecs_specs'),
    ]

    operations = [
        migrations.AddField(
            model_name='solspecs',
            name='Title',
            field=models.CharField(default=1, max_length=100, verbose_name='Характеристика IT продудкта'),
            preserve_default=False,
        ),
    ]