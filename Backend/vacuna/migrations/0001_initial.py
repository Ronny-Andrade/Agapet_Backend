# Generated by Django 4.1.4 on 2023-01-08 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pet', '0002_alter_mascota_options_mascota_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('vacuna_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_vacuna', models.CharField(max_length=200)),
                ('descripcion_vacuna', models.CharField(max_length=200)),
                ('idanimal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.animal')),
            ],
            options={
                'db_table': 'vacuna',
            },
        ),
        migrations.CreateModel(
            name='Vacuna_Mascota',
            fields=[
                ('vacuna_mascota_id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen_blob', models.BinaryField(blank=True, null=True)),
                ('feche_inicio', models.DateField(blank=True, null=True)),
                ('feche_fin', models.DateField(blank=True, null=True)),
                ('idpet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.mascota')),
                ('vacuna_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacuna.vacuna')),
            ],
            options={
                'db_table': 'vacuna_mascota',
            },
        ),
    ]