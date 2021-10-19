from django.views.generic.base import TemplateView

from django.views.generic import ListView, DetailView, TemplateView
from article.models import Article


# class Home(TemplateView):
#     template_name = 'home.html'

class Introduce(TemplateView):
    template_name = 'introduce.html'

class ArticleListPreview(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'