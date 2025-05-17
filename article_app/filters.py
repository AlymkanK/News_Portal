import django_filters
from django.db.models import Q
from django.db import models
from article_app.models import Articles


class ArticleFilter(django_filters.FilterSet):
    search_filter = django_filters.CharFilter(method='filter_by_all', label = 'Поиск')

    class Meta:
        model = Articles
        fields = ['title', 'content']




    def filter_by_all(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(content__icontains=value)
        )