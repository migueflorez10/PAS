# Generated by Django 4.2.4 on 2023-09-05 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=50)),
                ('nombreEmpresa', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
    ]