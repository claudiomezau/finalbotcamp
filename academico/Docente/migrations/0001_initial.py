# Generated by Django 4.0.6 on 2022-07-21 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotografia', models.ImageField(upload_to='docentes')),
                ('rut', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('grado_academico', models.CharField(choices=[('Tecnico', 'Tecnico'), ('Profesional', 'Profesional'), ('Magister', 'Magister'), ('Doctor', 'Doctor')], max_length=50)),
            ],
        ),
    ]
