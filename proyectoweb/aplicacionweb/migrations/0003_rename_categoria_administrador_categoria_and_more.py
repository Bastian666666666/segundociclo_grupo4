# Generated by Django 5.0.4 on 2024-04-09 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionweb', '0002_categoria_usuario_avatarusuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrador',
            old_name='Categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Categoria',
            new_name='categoria',
        ),
    ]
