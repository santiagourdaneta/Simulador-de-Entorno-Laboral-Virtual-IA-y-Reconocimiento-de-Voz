# Generated by Django 5.2 on 2025-06-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TareaSimulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('respuesta_esperada', models.TextField()),
                ('dificultad', models.CharField(max_length=50)),
            ],
        ),
    ]
