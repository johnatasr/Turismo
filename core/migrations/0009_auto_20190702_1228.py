# Generated by Django 2.2.2 on 2019-07-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190702_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identificacao',
            name='num',
            field=models.IntegerField(default=0, verbose_name='Número'),
        ),
    ]
