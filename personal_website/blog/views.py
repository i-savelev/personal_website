from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def article_list(request):
    articles_list = Article.objects.all().order_by('-pub_date')[:5]
    context = {
        'articles_list': articles_list,
        }
    return render(request, 'blog/index.html', context)
    