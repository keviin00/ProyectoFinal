# Generated by Django 4.2.5 on 2023-10-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaAPP', '0005_alter_customuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='direccion',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
