# Generated by Django 3.2.7 on 2023-01-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20230104_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregas',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
