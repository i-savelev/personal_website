from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
import re
import base64
from django.conf import settings
import uuid
from pathlib import Path


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=250)
    short_title = models.CharField(default='article')
    pub_date = models.DateTimeField(default=timezone.now)
    description = HTMLField()
    content = HTMLField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    draft = models.BooleanField()

    def save(self, *args, **kwargs):
        """
        added image saving from tinymce editor to a file
        """
        self.short_title = self.short_title.replace(' ', '_')
        self.content = self.b64_to_file(self.content)
        self.description = self.b64_to_file(self.description)
        super(Article, self).save(*args, **kwargs)

    def b64_to_file(self, content):
        """
        Convert base64 image to standart png fomat.
        Saving png in folder and replace all source url in <img>
        """
        pattern = r'src="(data:image/[^"]+)"'
        b64_images = re.findall(pattern, content)
        for b64_image_one in b64_images:
            img_data = b64_image_one.split(',', maxsplit=1)[1]
            img_GUID = str(uuid.uuid4())
            img_name = f'article_{self.short_title}_{img_GUID}.png'
            img_save_URL = Path(settings.MEDIA_ROOT)/'articles'/img_name
            img_URL = f'{settings.MEDIA_URL}articles/{img_name}'
            with open(img_save_URL, "wb") as fh:
                fh.write(base64.decodebytes(img_data.encode()))
            content = content.replace(b64_image_one, img_URL)
        return content

    def __str__(self):
        return self.title