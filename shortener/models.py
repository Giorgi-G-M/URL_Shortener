from django.db import models

# Create your models here.
class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.original_url} to {self.short_url}"