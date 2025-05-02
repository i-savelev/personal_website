from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Article, Tag

class ArticleAdmin(MarkdownxModelAdmin):
    fields = ['title', 'short_title', "pub_date","pub", "tags","description", "content"]
    list_display = ('title','id', 'get_tags', 'pub_date', 'pub') 
    filter_horizontal = ("tags",)
    list_filter = ["pub"]
    
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)