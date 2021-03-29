from rest_framework import serializers
from .models import Card
from imagekit.models import ProcessedImageField

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('__all__')


# class CardBodySerializer(serializers.Serializer):
#     # sessionkey = serializers.CharField(help_text="sessionkey")
#     input_image_1 = serializers.ImageField(help_text="input_image_1")
#     input_image_2 = serializers.ImageField(help_text="input_image_2")
#     input_image_3 = serializers.ImageField(help_text="input_image_3")
#     input_image_4 = serializers.ImageField(help_text="input_image_3")
#     output_image_1 = serializers.ImageField(help_text="input_image_1")
#     output_image_2 = serializers.ImageField(help_text="input_image_2")
#     output_image_3 = serializers.ImageField(help_text="input_image_3")
#     output_image_4 = serializers.ImageField(help_text="input_image_4")


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField(help_text='image')