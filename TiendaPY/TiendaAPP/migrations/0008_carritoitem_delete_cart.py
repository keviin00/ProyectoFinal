# Generated by Django 4.2.5 on 2023-10-14 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaAPP', '0007_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_id', models.PositiveIntegerField()),
                ('cantidad', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
