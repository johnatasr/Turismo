# Generated by Django 2.2.2 on 2019-07-01 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_identificacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='identi',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Identificacao'),
        ),
    ]