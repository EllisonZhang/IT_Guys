# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-09 12:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('year_released', models.DateField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('game_reviewed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WeGame.Games')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfBirth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WeGame.UserProfile'),
        ),
        migrations.AddField(
            model_name='games',
            name='publisher_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WeGame.Publishers'),
        ),
    ]
