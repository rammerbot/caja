# Generated by Django 4.1.7 on 2023-03-05 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caja', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caja',
            old_name='timbet',
            new_name='tinbet',
        ),
        migrations.AddField(
            model_name='caja',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]