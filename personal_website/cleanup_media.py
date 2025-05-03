import os
import re
from pathlib import Path
import django
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()


from blog.models import Article

used_images = set()
for post in Article.objects.all():
    matches = re.findall(r"/data/articles/([^)\s]+)", post.content)
    matches.extend(re.findall(r"/data/articles/([^)\s]+)", post.description))
    for filename in matches:
        used_images.add(filename)

folder_path = Path(settings.MEDIA_ROOT)/'articles'
for file_path in folder_path.rglob("*.png"):
    if file_path.is_file():
        relative_path = str(file_path.relative_to(folder_path))
        if relative_path not in used_images:
            print(f"Deleting: {relative_path}")
            file_path.unlink()