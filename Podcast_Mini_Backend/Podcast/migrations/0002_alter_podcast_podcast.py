# Generated by Django 3.2.5 on 2023-03-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Podcast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='podcast',
            field=models.FileField(upload_to='podcasts/'),
        ),
    ]