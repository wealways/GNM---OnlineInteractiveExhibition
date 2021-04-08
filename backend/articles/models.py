from django.db import models

# Create your models here.
class Guestbook(models.Model):
    user_nickname = models.CharField(max_length=15)
    guestbook_comment = models.CharField(max_length=144)
    guestbook_password = models.CharField(max_length=20)
    guestbook_image = models.CharField(max_length=500 ,null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)