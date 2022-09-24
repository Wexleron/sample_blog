from django.contrib import admin
from .models import ArticleModel, ArticleTagModel

#Custom admin save function
class ArticleAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(ArticleModel, ArticleAdmin) #Custom admin form save is determined by 2nd positional arg.)
admin.site.register(ArticleTagModel)