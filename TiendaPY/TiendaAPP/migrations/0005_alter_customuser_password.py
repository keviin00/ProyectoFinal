# Generated by Django 4.2.5 on 2023-10-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaAPP', '0004_remove_customuser_contrasena_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='123456', max_length=255),
        ),
    ]