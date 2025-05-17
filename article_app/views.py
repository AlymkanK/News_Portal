from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django_filters.views import FilterView

from .models import Articles, Category
from .forms import ArticlesForm, CategoriesForm
from django.db.models import Q

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

    def form_valid(self, form):
        category_name = form.cleaned_data.pop('category')
        category, created = Category.objects.get_or_create(name=category_name)
        form.instance.category = category
        return super().form_valid(form)


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
    success_url = reverse_lazy('article_app:articles')


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'article_app/delete.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article_app:articles')

    # def articles_delete_view(request, pk):
    #     article = Articles.objects.get(pk=pk)
    #     article.delete()
    #     return redirect('articles_app:articles')

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author






class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoriesForm
    template_name = 'article_app/create_category.html'
    context_object_name = 'category'
    success_url = reverse_lazy('articles_app:create')

class CategoryListView(ListView):
    model = Category
    template_name = 'article_app:categories.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = ('article_app/create_category.html')
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Articles.objects.filter(category=self.object)
        return context


class ArticleSearchView(FilterView):
    model = Articles
    template_name = 'article_app/search_results.html'
    context_object_name = 'article'





# def article_list(request):
#     filt = ArticleFilter(requestt.GETT, queryset = Articles.objects.all())
#     return redirect('article_app/base.html', {'filter': filt})