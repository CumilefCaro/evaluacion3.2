# Generated by Django 3.1.2 on 2023-06-21 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]