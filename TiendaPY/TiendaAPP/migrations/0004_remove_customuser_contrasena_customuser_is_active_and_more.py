# Generated by Django 4.2.5 on 2023-10-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaAPP', '0003_carritoitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='contrasena',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='valor_contraseña_predeterminado', max_length=255),
        ),
        migrations.DeleteModel(
            name='CarritoItem',
        ),
    ]
