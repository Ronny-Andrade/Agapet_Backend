# Generated by Django 4.1.4 on 2023-01-13 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_imagen64_alter_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
