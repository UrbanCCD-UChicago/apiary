# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 20:12
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField()),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField()),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiary.Network')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
                ('primitive', models.CharField(max_length=255)),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField()),
                ('features', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiary.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField()),
                ('nodes', models.ManyToManyField(to='apiary.Node')),
            ],
        ),
        migrations.AddField(
            model_name='feature',
            name='sensors',
            field=models.ManyToManyField(to='apiary.Sensor'),
        ),
    ]
