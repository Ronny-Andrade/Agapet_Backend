# Generated by Django 4.1.4 on 2023-01-17 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacuna', '0004_vacuna_lugar_vacuna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacuna',
            name='descripcion_vacuna',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
