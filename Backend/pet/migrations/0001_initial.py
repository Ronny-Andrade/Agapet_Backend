# Generated by Django 4.1.4 on 2023-01-05 00:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('idanimal', models.AutoField(primary_key=True, serialize=False)),
                ('tipoanimal', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Animal',
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idpet', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], max_length=1)),
                ('estado', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=200)),
                ('edad', models.PositiveIntegerField()),
                ('peso', models.FloatField()),
                ('comida', models.CharField(max_length=50)),
                ('deportivo', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('jugueton', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('sociable', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('miedoso', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('esterelizado', models.CharField(max_length=1)),
                ('fecha_esterelizado', models.DateField(blank=True, null=True)),
                ('lugar_esterelizado', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_esterelizado', models.CharField(blank=True, max_length=200, null=True)),
                ('desparacitado', models.CharField(max_length=1)),
                ('fecha_desparacitado', models.DateField(blank=True, null=True)),
                ('lugar_desparacitado', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion_desparacitado', models.CharField(blank=True, max_length=200, null=True)),
                ('idanimal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.animal')),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pet',
                'verbose_name_plural': 'Pets',
                'db_table': 'pet',
            },
        ),
    ]
