from django.urls import path
from django.contrib.auth import views as auth   #used in view for "logout"
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('logout/', auth.LogoutView.as_view(template_name ='base.html'), name ='logout'),
    path('login/', views.blog_login, name='login'),
    path('signup/', views.signup, name="signup"),
    path("detail/<int:blog_id>/", views.blog_detail, name="blog_detail"),
    path("list/<int:tag_id>/", views.article_list, name="article_list"),
]