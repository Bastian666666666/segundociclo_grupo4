# Generated by Django 5.0.4 on 2024-04-09 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionweb', '0003_rename_categoria_administrador_categoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
