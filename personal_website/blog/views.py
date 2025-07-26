from django.shortcuts import render, get_object_or_404
from .models import Article
from .models import Tag
from django.core.paginator import Paginator
import re

def article_list(request):
    '''
    Renders a paginated list of published articles, along with all available tags.
    Uses a custom pagination range for navigation links.

    Args
    - request: The HTTP request object.

    return: An HttpResponse object rendering the 'blog/blog.html' template with context data.
    '''
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
    '''
    Renders a paginated list of published articles filtered by a specific tag name, along with all available tags.
    Uses a custom pagination range for navigation links.

    Args
    - request: The HTTP request object.
    - tag_name: The name of the tag to filter articles by.

    return: An HttpResponse object rendering the 'blog/blog.html' template with context data.
    '''
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
    '''
    Renders a paginated list of all published articles.
    Uses a custom pagination range for navigation links. Intended for an 'all posts' view with a higher page size.

    Args
    - request: The HTTP request object.

    return: An HttpResponse object rendering the 'blog/blog_all_posts.html' template with context data.
    '''
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

def article(request, short_title):
    '''
    Renders a single article page based on its unique short title.
    Extracts the first image URL from the article's description to use as a preview/thumbnail.

    Args
    - request: The HTTP request object.
    - short_title: The unique short title slug of the article to retrieve.

    return: An HttpResponse object rendering the 'blog/article.html' template with the article and its first image.
    '''
    article = get_object_or_404(Article, short_title=short_title)
    first_image = get_description_first_image(article.description)
    context = {
        'article': article,
        'first_image': first_image,
        }
        
    return render(request, 'blog/article.html', context)

def get_description_first_image(markdown_text):
    '''
    Extracts the URL of the first image found within a Markdown text string.
    Looks for the standard Markdown image syntax: ![alt text](image_url).

    Args
    - markdown_text: A string containing Markdown formatted text.

    return: The URL of the first image found, or None if no image is found.
    '''
    pattern = r'!\[.*?\]\((.*?)\)'
    match = re.search(pattern, markdown_text)
    if match:
        return match.group(1)
    return None

def error_404_view(request, exception):
    '''
    Handles 404 Not Found errors by rendering a custom 404 error page.

    Args:
    - request: The HTTP request object that resulted in a 404 error.
    - exception: The exception object representing the error (e.g., Http404).

    return: An HttpResponse object rendering the '404.html' template.
    '''
    return render(request, '404.html')