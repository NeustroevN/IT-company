# Generated by Django 5.0.4 on 2024-05-09 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITapp', '0008_alter_aboutcompany_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutcompany',
            options={'verbose_name': 'О компании', 'verbose_name_plural': 'О компании'},
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='description',
            field=models.TextField(verbose_name='О компании'),
        ),
    ]