# Generated by Django 5.0.4 on 2024-04-10 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionweb', '0004_remove_usuario_categoria_delete_administrador_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseñaUsuario',
            new_name='contrasenaUsuario',
        ),
    ]
