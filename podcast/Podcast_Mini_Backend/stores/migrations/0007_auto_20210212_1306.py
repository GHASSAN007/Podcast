# Generated by Django 3.1.5 on 2021-02-12 13:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0006_auto_20210207_2345'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='stores',
            new_name='stores_info',
        ),
    ]