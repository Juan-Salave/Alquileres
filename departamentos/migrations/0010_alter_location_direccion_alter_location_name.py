# Generated by Django 4.2 on 2024-06-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0009_alter_location_options_alter_location_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='direccion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Deptomoede'),
        ),
    ]
