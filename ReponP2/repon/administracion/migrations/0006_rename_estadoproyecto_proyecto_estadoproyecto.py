# Generated by Django 4.2.4 on 2023-09-07 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0005_alter_proyecto_estadoproyecto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='EstadoProyecto',
            new_name='estadoProyecto',
        ),
    ]