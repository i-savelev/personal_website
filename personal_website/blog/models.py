from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    description = HTMLField()
    content = HTMLField()
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    draft = models.BooleanField()
    
    def __str__(self):
        return self.title

