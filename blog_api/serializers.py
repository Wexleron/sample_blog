from rest_framework import serializers
from blog.models import ArticleModel, ArticleTagModel
from rest_framework.reverse import reverse

""" ARTICLE LIST SERIALIZERS FOLLOWS BELLOW """

class TagSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ArticleTagModel
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    #sets tag field to be serialized by its own serialiser
    tag = TagSerialiser(read_only=True, many=True)
    
    class Meta:
        model = ArticleModel
        fields = [
            "title",
            "text",
            "tag",
            "image",
            "image_thumbnail",
            "created",
            "author_name",  #custom field
            "absolute_url", #custom field
        ]
    #function defining what to be seen in custom field
    def get_absolute_url(self, obj):
        return reverse("articles_api_detail", args=(obj.pk,))
    #function returning author username isntead of PK
    def get_author_name(self, obj):
        return obj.author.username