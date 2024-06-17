from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Omboli_Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class OmboliMessage(models.Model):
    room = models.ForeignKey(Omboli_Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)