from django.contrib import admin

from article_app.models import Articles, Category


# Register your models here.

admin.site.register(Articles)
admin.site.register(Category)
