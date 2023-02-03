from django.shortcuts import render

from hexlet_django_blog.article.apps import ArticleConfig
# Create your views here.


def index(request):
    return render(request, 'article/index.html', context={
        'app_name': ArticleConfig.name,
    })
