from rest_framework import serializers
from .models import Guestbook

class GuestbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guestbook
        fields = ('user_nickname', 'guestbook_comment', 'guestbook_image', 'id', 'created_date', 'updated_date')
        
