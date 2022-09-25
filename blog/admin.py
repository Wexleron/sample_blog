from django.contrib import admin
from .models import ArticleModel, ArticleTagModel

#Custom admin save function
class ArticleAdmin(admin.ModelAdmin):
    #Custom query set to show only articles that belongs to logged-in user
    def get_queryset(self, request):
        custom_querry = super(ArticleAdmin, self).get_queryset(request)
        return custom_querry.filter(author=request.user.pk)

    #Custom save model to put autor ID to article
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(ArticleModel, ArticleAdmin)
admin.site.register(ArticleTagModel)