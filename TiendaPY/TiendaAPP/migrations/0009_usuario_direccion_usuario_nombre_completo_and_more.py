# Generated by Django 4.2.5 on 2023-10-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaAPP', '0008_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(default='test', max_length=255),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre_completo',
            field=models.CharField(default='test', max_length=255),
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='test', max_length=50, unique=True),
        ),
    ]