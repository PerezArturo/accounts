# Generated by Django 2.2.6 on 2019-10-28 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='nombre',
            field=models.CharField(max_length=3),
        ),
    ]
