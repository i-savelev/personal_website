from django.contrib import admin

from .models import Article, Tag

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'short_title', "pub_date","draft", "tags","description", "content"]
    list_display = ('title','id', 'get_tags', 'pub_date', 'draft') 
    filter_horizontal = ("tags",)
    list_filter = ["draft"]
    
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)