# Generated by Django 4.1.7 on 2023-03-08 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0003_alter_caja_options_caja_calabaza_caja_centimos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='mesa',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Mesa'),
        ),
    ]
