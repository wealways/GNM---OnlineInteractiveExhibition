from django.db import models
from imagekit.models import ProcessedImageField

# Create your models here.
class Card(models.Model):
    sessionkey = models.CharField(max_length=50, blank=True)
    input_image_1 = ProcessedImageField(upload_to="input", null=True, blank=True)
    input_image_2 = ProcessedImageField(upload_to="input", null=True, blank=True)
    input_image_3 = ProcessedImageField(upload_to="input", null=True, blank=True)
    input_image_4 = ProcessedImageField(upload_to="input", null=True, blank=True)
    output_image_1 = ProcessedImageField(upload_to="output", null=True, blank=True)
    output_image_2 = ProcessedImageField(upload_to="output", null=True, blank=True)
    output_image_3 = ProcessedImageField(upload_to="output", null=True, blank=True)
    output_image_4 = ProcessedImageField(upload_to="output", null=True, blank=True)

class Art(models.Model):
    artist = models.CharField(max_length=50)
    art_image = models.CharField(max_length=50)
    art_description = models.CharField(max_length=50)
    art_voice_description = models.CharField(max_length=50)
    
