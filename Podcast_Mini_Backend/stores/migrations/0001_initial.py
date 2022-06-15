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
            name='stores_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('suptitle', models.TextField(default=models.CharField(max_length=200, unique=True))),
                ('stores', models.FileField(upload_to='stores_audio/', validators=[Scripts.validators.validate_podcast_extension])),
                ('Thumbnail', models.ImageField(upload_to='stores_Thumbnail/', validators=[Scripts.validators.validate_thumbnail_extension])),
                ('posting_date', models.DateTimeField(auto_now=True)),
                ('is_listened', models.BooleanField(default=False)),
                ('is_liked', models.BooleanField(default=False)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('listened', models.PositiveIntegerField(default=0)),
                ('language', models.CharField(choices=[('EN', 'English'), ('AR', 'Arabic'), ('ZH', 'Chines'), ('NL', 'Dutch'), ('FR', 'French'), ('DE', 'German'), ('RU', 'Russian'), ('JA', 'Japanese')], max_length=3)),
                ('is_stores_blocked', models.BooleanField(default=False)),
                ('is_private_story', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='story_comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date_of_comment', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('is_story_comment_blocked', models.BooleanField(default=False)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.stores_info')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='story_channels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('channel_name', models.CharField(max_length=250, unique=True)),
                ('subscribers', models.PositiveIntegerField(default=0)),
                ('creation_date', models.DateField(auto_now=True)),
                ('podcast_num', models.PositiveIntegerField(default=0)),
                ('storyteller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='stores_info',
            name='channels',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.story_channels'),
        ),
        migrations.AddField(
            model_name='stores_info',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.story_comments'),
        ),
        migrations.AddField(
            model_name='stores_info',
            name='podcasted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]