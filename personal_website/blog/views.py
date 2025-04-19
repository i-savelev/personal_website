from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from django.core.paginator import Paginator

def article_list(request):
    articles_list = Article.objects.filter(draft=True).order_by('-pub_date')
    paginator = Paginator(articles_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    pages_list = paginator.get_elided_page_range(number = page_obj.number, on_each_side=1, on_ends=1)
    context = {
        'articles_list': page_obj,
        'pages_list': pages_list,
        }
    return render(request, 'blog/blog.html', context)
    

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
        }
    return render(request, 'blog/article.html', context)