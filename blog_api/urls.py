from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticlesApiList.as_view(), name="articles_api_list"),
    path("detail/<int:pk>/", views.ArticlesApiDetail.as_view(), name="articles_api_detail"), 
]