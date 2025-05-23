# Generated by Django 5.2 on 2025-05-16 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название рекламы')),
                ('name', models.CharField(max_length=100, verbose_name='Имя рекламы')),
                ('content', models.TextField(verbose_name='Контент рекламы')),
                ('image', models.ImageField(upload_to='advertisement/images')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Категория')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('author', models.CharField(default=None, max_length=50, verbose_name='Автор')),
                ('content', models.TextField(max_length=1000, verbose_name='Описание')),
                ('images', models.ImageField(blank=True, null=True, upload_to='articles_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_app.category', verbose_name='Категория')),
            ],
        ),
    ]
