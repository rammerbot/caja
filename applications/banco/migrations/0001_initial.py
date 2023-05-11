# Generated by Django 4.1.7 on 2023-03-13 02:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fecha', models.DateField(unique=True, verbose_name='Fecha')),
                ('inicio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('ingreso', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('disponible', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Banco',
                'verbose_name_plural': 'Bancos',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('sucursal', models.CharField(max_length=30, verbose_name='Sucursal')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('deposito', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('fecha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.banco')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.sucursal')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
