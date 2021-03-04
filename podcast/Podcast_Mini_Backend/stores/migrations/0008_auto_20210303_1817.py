# Generated by Django 3.1.5 on 2021-03-03 18:17

import CODE_FOR_APPS.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_auto_20210212_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores_info',
            name='Thumbnail',
            field=models.ImageField(upload_to='media/stores_Thumbnail/', validators=[CODE_FOR_APPS.validators.validate_thumbnail_extension]),
        ),
        migrations.AlterField(
            model_name='stores_info',
            name='stores',
            field=models.FileField(upload_to='media/stores_audio/', validators=[CODE_FOR_APPS.validators.validate_podcast_extension]),
        ),
    ]
