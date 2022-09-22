from django.contrib import admin
from .models import ArticleModel, ArticleTagModel

admin.site.register(ArticleModel)
admin.site.register(ArticleTagModel)