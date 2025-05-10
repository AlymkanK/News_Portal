from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    form_class = ArticlesForm
    template_name= 'article_app/create.html'
    success_url = reverse_lazy('articles_app:articles')

    def form_valid(self, form):
        form.instance.user= self.request.user
        response = super().form_valid(form)

        article_details = (
            f'Заголовок: {form.instance.articles.title}\n'
            f'Название: {form.instance.articles.name}\n'
            f'Фото: {form.instance.articles.images}\n'
            f'Категория: {form.instance.articles.category}\n'
            f'Автор: {form.instance.articles.author}'

        )


class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'article_app/update.html'
    form_class = ArticlesForm


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'article_app/delete.html'
    context_object_name = 'article'

