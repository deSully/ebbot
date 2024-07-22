from django.db import models
import uuid

class Client(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone_number})"

class Issue(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='issues')
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    photos = models.ImageField(upload_to='issue_photos/', null=True, blank=True)
    videos = models.FileField(upload_to='issue_videos/', null=True, blank=True)
    audios = models.FileField(upload_to='issue_audios/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue for {self.title}"

class Message(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True)
    media_url = models.URLField(null=True, blank=True)
    media_type = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Message for Issue {self.issue.id} at {self.sent_at}"
