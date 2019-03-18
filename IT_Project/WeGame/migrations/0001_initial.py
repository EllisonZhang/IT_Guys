# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 16:35
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
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('year_released', models.DateField(max_length=30)),
                ('game_content', models.TextField(default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=100)),
                ('news_content', models.TextField(default='', null=True)),
                ('news_data', models.DateField(max_length=30)),
                ('editor_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=30)),
                ('picture_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_likes', models.IntegerField(default=0)),
                ('number_dislikes', models.IntegerField(default=0)),
                ('comment_text', models.CharField(max_length=500)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('game_reviewed', models.CharField(max_length=30)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=30)),
                ('video_path', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='publisher_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WeGame.Publisher'),
        ),
    ]
