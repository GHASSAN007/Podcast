# Generated by Django 4.0.1 on 2022-07-09 00:36

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
                ('subscribers', models.PositiveIntegerField(default=0)),
                ('creation_date', models.DateField(auto_now=True)),
                ('podcast_num', models.PositiveIntegerField(default=0)),
                ('is_story_channel_blocked', models.BooleanField(default=False)),
                ('storyteller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
