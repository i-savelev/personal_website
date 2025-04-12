from django.contrib import admin

from .models import Article, Tag

admin.site.register(Article) # Регистрация моделей в админке
admin.site.register(Tag)
