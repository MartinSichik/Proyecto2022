# Generated by Django 3.2.7 on 2023-01-10 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20230109_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Telefono',
            new_name='telefono',
        ),
    ]
