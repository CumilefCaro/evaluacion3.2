# Generated by Django 3.1.2 on 2023-06-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230620_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_germ',
            field=models.DateField(null=True),
        ),
    ]
