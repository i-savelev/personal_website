from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

def article_list(request):
    articles_list = Article.objects.filter(draft=True).order_by('-pub_date')[:5]
    
    context = {
        'articles_list': articles_list,
        }
    return render(request, 'blog/blog.html', context)
    

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
        }
    return render(request, 'blog/article.html', context)