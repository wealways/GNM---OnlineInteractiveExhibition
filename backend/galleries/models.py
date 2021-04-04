from django.db import models
from imagekit.models import ProcessedImageField

# 동적 파일 저장 위치 지정
import os

# 저장위치 dynamic path
def create_path(instance, filename):
    # input일 때
    print(instance.sessionkey)
    return os.path.join(str(instance.sessionkey), filename)

# Create your models here.
# 파일 해상도 보존을 위해 필드 변경(Processed Field => imagefield)
# column 4 => 3
class Card(models.Model):
    sessionkey = models.CharField(max_length=50, blank=True)
    input_image_1 = ProcessedImageField(upload_to=create_path, null=True, blank=True, format="JPEG")
    input_image_2 = ProcessedImageField(upload_to=create_path, null=True, blank=True, format="JPEG")
    input_image_3 = ProcessedImageField(upload_to=create_path, null=True, blank=True, format="JPEG")
    output_image_1 = ProcessedImageField(upload_to=create_path, null=True, blank=True, format="JPEG")
    output_image_2 = ProcessedImageField(upload_to=create_path, null=True, blank=True, format="JPEG")
    output_image_3 = ProcessedImageField(upload_to=create_path, null=True, blank=True, format="JPEG")


class Art(models.Model):
    artist = models.CharField(max_length=50)
    art_image = models.CharField(max_length=50)
    art_description = models.CharField(max_length=50)
    art_voice_description = models.CharField(max_length=50)
    
