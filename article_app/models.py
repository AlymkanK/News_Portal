import random, string

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Категория')
    slug = models.SlugField(max_length=50, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        # indexes = models.Index(
        # #    fields = ['name']
        # # )

class Articles(models.Model):
    slug = models.SlugField(max_length=200, unique = True, verbose_name='URL')
    title  = models.CharField(max_length=100, verbose_name='Заголовок')
    name = models.CharField(max_length=50, verbose_name='Название')
    #author = models.CharField(max_length=50, default=None, verbose_name='Автор')
    content = models.TextField(max_length=1000, verbose_name='Описание')
    images= models.ImageField(upload_to='articles_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    @classmethod
    def clean_save_slug(cls, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))


    def save(self, *args, **kwargs):
        if not self.slug or self.slug == '':
            len_name = len(self.name)
            Articles.clean_save_slug(len(self.name))
            self.slug = slugify(self.name).join
        super().save(*args, **kwargs)

class Advertisement(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название рекламы')
    name = models.CharField(max_length=100, verbose_name = 'Имя рекламы')
    content = models.TextField(verbose_name = 'Контент рекламы')
    image = models.ImageField(upload_to='advertisement/images')



