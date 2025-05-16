from django.urls import path, include

from . import views

app_name = 'article_app'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name = 'articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name = 'article'),
    path('article/create/', views.ArticleCreateView.as_view(), name = 'create'),
    path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name = 'update'),
    path('article/<int:pk>/delete', views.ArticleDeleteView.as_view(), name = 'delete'),
    path('contacts/', views.contacts, name='contacts'),
    path('article/category/create', views.CategoryCreateView.as_view(), name = 'category_create'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
]
