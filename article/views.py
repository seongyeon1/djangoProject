from django.views.generic import ListView, DetailView, TemplateView

from .models import Article

from django.shortcuts import render

#-- ListView
class ArticleList(ListView):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = 'articles'