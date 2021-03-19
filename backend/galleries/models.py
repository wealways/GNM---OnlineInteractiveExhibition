from django.db import models

# Create your models here.
class Card(models.Model):
    session_id = models.CharField(max_length=50)
    input_image_1 = models.CharField(max_length=100)
    input_image_2 = models.CharField(max_length=100)
    input_image_3 = models.CharField(max_length=100)
    input_image_4 = models.CharField(max_length=100)
    output_image_1 = models.CharField(max_length=100)
    output_image_2 = models.CharField(max_length=100)
    output_image_3 = models.CharField(max_length=100)
    output_image_4 = models.CharField(max_length=100)

class Art(models.Model):
    artist = models.CharField(max_length=50)
    art_image = models.CharField(max_length=50)
    art_description = models.CharField(max_length=50)
    art_voice_description = models.CharField(max_length=50)
    
