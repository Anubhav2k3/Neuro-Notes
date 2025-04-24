from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import json

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # AI-generated fields
    summary = models.TextField(blank=True, null=True)
    analysis = models.TextField(blank=True, null=True)

    # Translations stored in a dictionary: {"fr": "French content", "hi": "Hindi content", ...}
    translations = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_translation(self, lang_code):
        if self.translations and lang_code in self.translations:
            return self.translations[lang_code]
        return None
