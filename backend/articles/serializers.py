from rest_framework import serializers
from .models import Guestbook

class GuestbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guestbook
        fields = ('user_nickname', 'guestbook_comment', 'guestbook_image', 'id', 'created_date', 'updated_date', 'guestbook_password')
        

class GuestbookBodySerializer(serializers.Serializer):
    user_nickname = serializers.CharField(help_text="user_nickname")
    guestbook_comment = serializers.CharField(help_text="guestbook_comment")
    guestbook_image = serializers.CharField(help_text="guestbook_image")