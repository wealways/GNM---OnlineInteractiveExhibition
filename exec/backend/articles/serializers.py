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
    guestbook_password = serializers.CharField(help_text="guestbook_password")


class PasswordSerializer(serializers.Serializer):
    guestbook_password =serializers.CharField(help_text="guestbook_password")


class GuestbookListSerializer(serializers.Serializer):
    page = serializers.CharField(help_text="page")
    articles_per_page = serializers.CharField(help_text="articles_per_page")