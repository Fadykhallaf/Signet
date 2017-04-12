# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-12 12:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        ('questions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('F', 'Favorite'), ('L', 'Like'), ('U', 'Up Vote'), ('D', 'Down Vote')], max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('feed', models.IntegerField(blank=True, null=True)),
                ('question', models.IntegerField(blank=True, null=True)),
                ('answer', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(choices=[('L', 'Liked'), ('C', 'Commented'), ('F', 'Favorited'), ('A', 'Answered'), ('W', 'Accepted Answer'), ('E', 'Edited Article'), ('S', 'Also Commented')], max_length=1)),
                ('is_read', models.BooleanField(default=False)),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Answer')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('feed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feeds.Feed')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ('-date',),
            },
        ),
    ]
