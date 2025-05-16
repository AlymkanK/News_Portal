from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Articles, Category
from .forms import ArticlesForm


class ArticleListView(ListView):
    model = Articles
    template_name= 'article_app/articles.html'
    context_object_name = 'articles'

class ArticleCreateView(CreateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'article_app/create.html'
    context_object_name = 'articles'
    success_url = reverse_lazy('article_app:articles')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
# def articles_create_view(request):
#     if request.method == 'POST':
#         form = ArticlesForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             name = form.cleaned_data['name']
#             content = form.cleaned_data['content']
#             category = form.cleaned_data['category']
#
#             news = Articles.objects.create(
#                 title=title,
#                 name=name,
#                 content=content,
#                 category=category,
#             )
#             news.save()
#             return redirect('article_app:articles')
#     else:
#         form = ArticlesForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'article_app:create', context)




class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'article_app/article.html'
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'article_app/update.html'
    form_class = ArticlesForm
    success_url = reverse_lazy('articles_app:articles')

class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'article_app/delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('articles_app:articles')

    def articles_delete_view(request, pk):
        article = Articles.objects.get(pk=pk)
        article.delete()
        return redirect('articles_app:articles')

def contacts(request):
    return redirect( 'article_app:contacts')

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'article_app/create_category.html'
    success_url = reverse_lazy('articles_app:create')
