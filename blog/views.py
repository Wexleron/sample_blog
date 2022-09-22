from django.shortcuts import render, redirect
from .models import ArticleModel

def index(request):
    #Iterate model for first 3 articles
    articles= ArticleModel.objects.all()[:3]

    contents = {
        'articles' : articles,
    }

    return render(request, "blog/base.html", contents)