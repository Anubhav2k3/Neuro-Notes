from django.db import models
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return self.title
    
    def get_content_preview(self, max_length=100):
        """Return a preview of the content for display"""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..."
