# Generated by Django 2.2.2 on 2019-06-26 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pontoturistico_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturistico',
            old_name='comentario',
            new_name='comentarios',
        ),
    ]
