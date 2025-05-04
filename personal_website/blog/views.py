from django.shortcuts import render, get_object_or_404
from .models import Article
from .models import Tag
from django.core.paginator import Paginator
import re

def article_list(request):
    articles_list = Article.objects.filter(pub=True).order_by('-pub_date')
    tags_list = Tag.objects.all()
    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    pages_list = paginator.get_elided_page_range(number = page_obj.number, on_each_side=1, on_ends=1)
    context = {
        'tags': tags_list,
        'page_obj': page_obj,
        'pages_list': pages_list,
        }
    return render(request, 'blog/blog.html', context)

def article_by_tag_list(request, tag_name):
    articles_list = Article.objects.filter(pub=True, tags__name__icontains = tag_name).order_by('-pub_date')
    tags_list = Tag.objects.all()
    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    pages_list = paginator.get_elided_page_range(number = page_obj.number, on_each_side=1, on_ends=1)

    context = {
        'tags': tags_list,
        'page_obj': page_obj,
        'pages_list': pages_list,
        'tag_name': tag_name,
        }
    return render(request, 'blog/blog.html', context)
    

def article_all(request):
    articles_list = Article.objects.filter(pub=True).order_by('-pub_date')
    paginator = Paginator(articles_list, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    pages_list = paginator.get_elided_page_range(number = page_obj.number, on_each_side=1, on_ends=1)
    context = {
        'page_obj': page_obj,
        'pages_list': pages_list,
        }
    print(f"Rendering template: blog/allposts.html")
    return render(request, 'blog/blog_all_posts.html', context)    

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    first_image = get_description_first_image(article.description)
    context = {
        'article': article,
        'first_image': first_image,
        }
        
    return render(request, 'blog/article.html', context)

def get_description_first_image(markdown_text):
    pattern = r'!\[.*?\]\((.*?)\)'
    match = re.search(pattern, markdown_text)
    if match:
        return match.group(1)
    return None