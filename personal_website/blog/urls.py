from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("blog/<int:article_id>", views.article, name="article"),
    path("blog/allposts", views.article_all, name="article_all"),
    path("blog/tag/<str:tag_name>", views.article_by_tag_list, name="article_by_tag_list"),
]