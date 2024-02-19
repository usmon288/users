from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Conversation(models.Model):
    user = models.ForeignKey(User, related_name='conversations', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.title} with User {self.user.username}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='messages/images/', blank=True, null=True)
    gif = models.FileField(upload_to='messages/gifs/', blank=True, null=True)
    video = models.FileField(upload_to='messages/videos/', blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message {self.id} in Conversation {self.conversation.id}"

    class Meta:
        ordering = ['timestamp']
