from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("blog/<int:article_id>", views.article, name="article"),
]