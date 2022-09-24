from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from .models import ArticleModel, ArticleTagModel
from .forms import UserSignupForm

def index(request):
    #Iterate model for first 3 articles
    articles= ArticleModel.objects.all().filter(active=True)[:3]
    tags = ArticleTagModel.objects.all()
    contents = {
        'articles' : articles,
		'tags' : tags,
    }

    return render(request, "blog/base.html", contents)

def blog_detail(request, blog_id):
	#Get Article detail by url "blog_id"
    article = ArticleModel.objects.get(pk=blog_id)
    tags = ArticleTagModel.objects.all()
    title = ArticleModel.objects.get(pk=blog_id)
    title = title.title
    contents = {
        'article' : article,
		'tags' : tags,
		'title' : title,
    }
    return render(request, "blog/blog_detail.html", contents)

def article_list(request, tag_id):
	#Get articles by tag
	articles = ArticleModel.objects.filter(tag=tag_id)
	tags = ArticleTagModel.objects.all()
	title = ArticleTagModel.objects.get(pk=tag_id)
	contents = {
        'articles' : articles,
		'tags' : tags,
		'title' : title,
    }
	return render(request, "blog/blog_list.html", contents)
	#Topping.objects.filter(on_pizza__restaurant=R).annotate(the_count=Count('on_pizza')).order_by('-the_count')[0]

def signup(request):
	if request.method == 'POST':
		signup_form = UserSignupForm(request.POST)
		if signup_form.is_valid():
			validated_signup_form = signup_form.save(commit=False)
			validated_signup_form.is_staff = True
			validated_signup_form.save()	#Save into DB with admin rights.
			user_group = Group.objects.get(name="Redaktoři")
			validated_signup_form.groups.add(user_group)
			validated_signup_form.save()	#Save again in DB with groups, which can be created only after user has ID (been created).
			return redirect('login')
	elif request.user.is_authenticated:
		return redirect('index')
	else:
		signup_form = UserSignupForm()
	return render(request, 'blog/signup.html', {'signup_form': signup_form,})

def blog_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			return redirect('login')
	else:
		if request.user.is_authenticated:
			return redirect('index')
		else:
			login_form = AuthenticationForm()
			return render(request, 'blog/login.html', {'login_form': login_form})