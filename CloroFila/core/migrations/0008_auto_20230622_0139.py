# Generated by Django 3.1.2 on 2023-06-22 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20230622_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_germ',
            field=models.DateField(default=True),
        ),
    ]
