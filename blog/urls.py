from django.urls import path
from django.contrib.auth import views as auth   #used in view for "logout"
from . import views

urlpatterns = [
    path("", views.index, name="index"),    #blog/base.html
    path('logout/', auth.LogoutView.as_view(template_name ='base.html'), name ='logout'),
    path('login/', views.blog_login, name='login'),
    path('signup/', views.signup, name="signup"),
    path("detail/<int:blog_id>/", views.blog_detail, name="blog_detail"),   #article detail
    path("list/", views.all_list, name="all_list"), #all articles
    path("list/<int:tag_id>/", views.article_list, name="article_list"), #articles by category
]