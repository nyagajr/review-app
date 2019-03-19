# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=30)),
                ('dpic', models.ImageField(upload_to='articles/')),
                ('contact_info', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('project_img', models.ImageField(upload_to='articles/')),
                ('description', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=30)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
        ),
    ]