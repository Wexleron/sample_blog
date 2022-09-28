from django.test import TestCase
from django.test import Client
from blog.models import ArticleModel, ArticleTagModel
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission
from tracemalloc import start as tracemalloc

#Used in "python -Wa manage.py test" to show depreciated and other things.
tracemalloc()

#Test new article creation, tag creation, article check_time().
class ModelsTestCase(TestCase):
    #initiates DB prod+dummy fixtures
    fixtures = ('prod_group.json', 'dummy_user', 'dummy_basic')
    def setUp(self):
        #creates testuser (It is not created by custom sign-up view!)
        user = User.objects.create_user(username='testuser', password='12345', is_staff = True)
        group = Group.objects.get(pk=1)
        user.groups.add(group)
        #creates tag
        tag = ArticleTagModel.objects.create(
            name = "Roboti",
        )
        #creates Article for test user
        article = ArticleModel.objects.create(
        title="Roboti útočí",
        text = "A bylo to velmi krátké, přidali se totiž i Androidi",
        author = User.objects.get(username = 'testuser'),
        active = True)
        #Insert tag into object (M2M)
        article.tag.add(tag)

#test n. 1
    def test_models(self):
        article = ArticleModel.objects.get(title='Roboti útočí')
        tag = ArticleTagModel.objects.get(name='Roboti')
        user = User.objects.get(username='testuser')
        #test tag model
        self.assertTrue(tag)
        self.assertEqual(tag.name, 'Roboti')
        #test article model
        self.assertEqual(article.author.username, "testuser")
        #test tag count M2M
        self.assertEqual(article.tag.count(), 1)
        #tests auto timestamp with current datetime; newly created article is always less than 24 hours fresh.
        self.assertEqual(article.check_time(), '<span style="color:green; font-weight:bold;">mladší než 24 hodin</span>')
        #test testusers group and staff
        self.assertTrue(user.is_staff)
#test n. 2
    def test_signup_endpoint(self):
        #initiate django class for dummy web browser
        client = Client()
        #test user registration by signup template.
        data = {
            "username": "Aleš",
            "password1": "heslojeveslo",
            "password2": "heslojeveslo",
        }
        response = client.post("/signup/", data)
        created_user = User.objects.get(username = 'Aleš')
        self.assertEqual(created_user.username, "Aleš")
        self.assertEqual(User.objects.count(), 8)
        self.assertRedirects(response, "/login/")
#test n. 3
    def test_get_endpoints(self):
        #initiate django class for dummy web browser
        client = Client()
        #tests detail template for article made in test n.1 == test_models().
        response = client.get("/detail/1/")
        self.assertEqual(response.status_code, 200)
        #tests list by tag
        response = client.get("/list/1/")
        self.assertEqual(response.status_code, 200)
        #test index
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
#test n. 4
    def test_logged_endpoints(self):
        #creates client instance for dummy-web browsing
        client = Client()
        #tests login-in testuser made in setUp()
        response = client.post("/login/", {"username": "testuser", "password": "12345",})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/admin/")
        #tests adding an article as logged-in user
        data = {
            'title' :  "Koně moje hravý",
            'text' : "Ještě asfhasf asag Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. ",
            'tag' : [1,2],
            'active' : True,}
        response = client.post("/admin/blog/articlemodel/add/", data)
        new_article = ArticleModel.objects.get(title = 'Koně moje hravý')
        self.assertEqual(response.status_code, 302)
        self.assertEqual("Koně moje hravý", new_article.title)

