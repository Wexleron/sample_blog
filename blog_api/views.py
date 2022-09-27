from rest_framework import generics
from blog.models import ArticleModel
from .serializers import ArticleSerializer

class ArticlesApiList(generics.ListAPIView):
    queryset = ArticleModel.objects.all().filter(active=True)
    serializer_class = ArticleSerializer

class ArticlesApiDetail(generics.RetrieveAPIView):
    queryset = ArticleModel.objects.all().filter(active=True)
    serializer_class = ArticleSerializer