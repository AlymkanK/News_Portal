from django import forms
from .models import Articles, Advertisement, Category


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = [ 'title', 'name', 'content',
        'images', 'category',
        ]

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'name', 'content', 'image']

