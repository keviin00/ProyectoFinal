# Generated by Django 4.2.5 on 2023-10-12 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaAPP', '0009_usuario_direccion_usuario_nombre_completo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre_completo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]
