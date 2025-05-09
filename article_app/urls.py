from django.urls import path

from . import views

app_name = 'article_app'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name = 'articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name = 'article'),
    path('article_create/', views.ArticleCreateView.as_view(), name = 'create'),
    path('article_update/<int:pk>', views.ArticleUpdateView.as_view(), name = 'update'),
    path('article_delete/<int:pk>', views.ArticleDeleteView.as_view(), name = 'delete'),
]
