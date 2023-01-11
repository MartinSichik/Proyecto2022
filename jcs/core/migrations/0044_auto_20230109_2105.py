# Generated by Django 3.2.7 on 2023-01-10 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20230106_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name=' Nombres ')),
                ('Telefono', models.CharField(max_length=150, unique=True, verbose_name=' Telefonos ')),
                ('Ruc', models.CharField(max_length=150, unique=True, verbose_name=' Ruc ')),
                ('email', models.CharField(max_length=150, unique=True, verbose_name=' email ')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'Proveedores',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='quimico',
            name='procedencia',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name=' Procedencia '),
        ),
        migrations.AlterField(
            model_name='quimico',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.catequimico'),
        ),
        migrations.AlterField(
            model_name='quimico',
            name='unidades',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.unidades'),
        ),
    ]
