# Generated by Django 5.0.4 on 2024-05-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITapp', '0009_alter_aboutcompany_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcompany',
            name='image',
            field=models.ImageField(upload_to='static/img/', verbose_name='Банер'),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='mapimg',
            field=models.ImageField(upload_to='static/img/', verbose_name='Карта'),
        ),
    ]
