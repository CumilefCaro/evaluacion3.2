# Generated by Django 3.1.2 on 2023-06-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20230622_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_germ',
            field=models.DateField(),
        ),
    ]
