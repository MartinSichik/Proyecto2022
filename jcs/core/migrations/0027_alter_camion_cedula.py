# Generated by Django 3.2.7 on 2023-01-03 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_entregas_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camion',
            name='cedula',
            field=models.CharField(max_length=7, unique=True, verbose_name=' cedula '),
        ),
    ]
