# Generated by Django 4.0.5 on 2022-07-28 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_alter_comentario_options_alter_usuario_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='marca',
        ),
        migrations.AddField(
            model_name='comentario',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Registrado'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comentarios.usuario', verbose_name='Usuario'),
        ),
    ]