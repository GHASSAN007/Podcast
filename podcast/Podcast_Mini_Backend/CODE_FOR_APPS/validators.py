import os
from django.core.exceptions import ValidationError

def validate_podcast_extension(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.mp3','.wav', '.aac','.amr', '.opus', '.webm', '.wma' ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported podcast/story format, Try to use .mp3 , .wav ... format . ')

def validate_thumbnail_extension(value):
    ext = os.path.splitext(value.name)[1]  
    valid_extensions = ['.jpg','.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported image format, Try to use .jpg , .png ... format ')

