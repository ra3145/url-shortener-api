from django.db import models


class URL(models.Model):
    longurl = models.TextField()
    shorturl = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.shorturl
# Create your models here.
