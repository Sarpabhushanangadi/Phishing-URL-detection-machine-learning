# detector/models.py
from django.db import models

class PhishingURL(models.Model):
    url = models.URLField()
    is_phishing = models.BooleanField(null=True, blank=True)
