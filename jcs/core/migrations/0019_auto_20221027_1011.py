# Generated by Django 3.2.7 on 2022-10-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_grano_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='grano',
            name='procedencia',
            field=models.CharField(default='', max_length=10, null=True, verbose_name=' procedencia '),
        ),
        migrations.AlterField(
            model_name='grano',
            name='variedad',
            field=models.CharField(max_length=10, verbose_name=' Variedad '),
        ),
    ]
