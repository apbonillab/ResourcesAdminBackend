# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-03 05:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Control_Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=1000)),
                ('descripcion', models.CharField(max_length=1000, null=True)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lista_Chequeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('idSolicitud', models.CharField(max_length=50)),
                ('idProyecto', models.CharField(max_length=50)),
                ('descripcionSolicitud', models.CharField(max_length=300)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estado', to='resourcesApp.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Recurso_Intermedio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesApp.Estado')),
                ('recursoPrincipal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesApp.Recurso')),
            ],
        ),
        migrations.CreateModel(
            name='Recurso_Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rescursos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesApp.Recurso')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado_ListaChequeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado', models.BooleanField()),
                ('itemChequeo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesApp.Lista_Chequeo')),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesApp.Recurso_Intermedio')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='responsable',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesApp.Rol'),
        ),
        migrations.AddField(
            model_name='recurso_responsable',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsables', to='resourcesApp.Responsable'),
        ),
        migrations.AddField(
            model_name='recurso_intermedio',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesApp.Responsable'),
        ),
        migrations.AddField(
            model_name='recurso_intermedio',
            name='tipoRecurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesApp.Tipo_Recurso'),
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipoRecurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipoRecurso', to='resourcesApp.Tipo_Recurso'),
        ),
        migrations.AddField(
            model_name='lista_chequeo',
            name='asignado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcesApp.Responsable'),
        ),
        migrations.AddField(
            model_name='control_comentarios',
            name='idRecurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recurso', to='resourcesApp.Recurso'),
        ),
        migrations.AddField(
            model_name='control_comentarios',
            name='revisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsable', to='resourcesApp.Responsable'),
        ),
    ]
