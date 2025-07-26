from django.db import models
from django.utils import timezone
import re
from django.conf import settings
import uuid
from pathlib import Path
from markdownx.models import MarkdownxField


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=250)
    short_title = models.CharField(unique=True, max_length=250)
    pub_date = models.DateTimeField(default=timezone.now)
    description = MarkdownxField()
    content = MarkdownxField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    pub = models.BooleanField()

    def save(self, *args, **kwargs):
        '''
        Saves the Article instance. Before saving, it searches for temporary image files
        (matching a specific UUID pattern) in the 'articles' media folder. If found,
        it renames these files to a permanent name based on the article's short_title
        and updates their references in the description and content fields.

        Args
        - *args: Variable length argument list passed to the parent save method.
        - **kwargs: Arbitrary keyword arguments passed to the parent save method.

        return: None
        '''
        pattern = re.compile(r'^[a-f0-9]{8}(?:-[a-f0-9]{4}){3}-[a-f0-9]{12}\.png$')
        folder_path = Path(settings.MEDIA_ROOT)/'articles'
        for file in folder_path.rglob('*'):
            if file.is_file() and pattern.match(file.name):
                img_GUID = str(uuid.uuid4())
                new_img_name = f'article_{self.short_title}_{img_GUID}.png'
                self.description = self.description.replace(file.name, new_img_name)
                self.content = self.content.replace(file.name, new_img_name)
                file.rename(f'{folder_path}/{new_img_name}')

        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title