from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Articles
from .forms import ArticlesForm

class ArticleListView(ListView):
    model = Articles
    template_name= 'article_app/articles.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'article_app/article.html'
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    model = Articles
    template_name= 'article_app/create.html'
    form_class = ArticlesForm


class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'article_app/update.html'
    form_class = ArticlesForm


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'article_app/delete.html'
    context_object_name = 'article'

