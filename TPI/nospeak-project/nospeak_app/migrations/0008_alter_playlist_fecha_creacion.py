# Generated by Django 4.2.4 on 2023-08-22 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nospeak_app', '0007_artista_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='fecha_creacion',
            field=models.DateField(null=True),
        ),
    ]
