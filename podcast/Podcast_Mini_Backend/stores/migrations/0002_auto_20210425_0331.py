# Generated by Django 3.2 on 2021-04-25 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='story_channels',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='story_comments',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
