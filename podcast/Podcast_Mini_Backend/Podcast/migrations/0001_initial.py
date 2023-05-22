# Generated by Django 4.0.1 on 2022-03-22 20:08

import Scripts.validators
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
            name='channel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('channel_name', models.CharField(max_length=250, unique=True)),
                ('subscribers', models.PositiveIntegerField(default=False)),
                ('creation_date', models.DateField(auto_now=True)),
                ('podcast_num', models.PositiveIntegerField(default=0)),
                ('is_podcast_channel_blocked', models.BooleanField(default=False)),
                ('podcast_maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200, unique=True)),
                ('Description', models.TextField(blank=True, default='No Description')),
                ('podcast', models.FileField(upload_to='podcasts/', validators=[Scripts.validators.validate_podcast_extension])),
                ('Thumbnail', models.ImageField(upload_to='Thumbnail/', validators=[Scripts.validators.validate_thumbnail_extension])),
                ('posting_date', models.DateTimeField(auto_now=True)),
                ('is_viewed', models.BooleanField(default=False)),
                ('is_liked', models.BooleanField(default=False)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('views', models.PositiveIntegerField(default=0)),
                ('language', models.CharField(choices=[('EN', 'English'), ('AR', 'Arabic'), ('ZH', 'Chines'), ('NL', 'Dutch'), ('FR', 'French'), ('DE', 'German'), ('RU', 'Russian'), ('JA', 'Japanese')], max_length=3)),
                ('is_podcast_blocked', models.BooleanField(default=False)),
                ('is_private_podcast', models.BooleanField(default=False)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Podcast.channel')),
                ('podcasted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date_of_comment', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('is_podcast_comment_blocked', models.BooleanField(default=False)),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Podcast.podcast_info')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]