from inspect import trace
from django.test import TestCase
from blog.models import ArticleModel, ArticleTagModel
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission
from tracemalloc import start as tracemalloc

#Used in "python -Wa manage.py test" to show depreciated and other things.
tracemalloc()

#Test new article creation, tag creation, article check_time().
class ModelsTestCase(TestCase):
    def setUp(self):
        #creates usergroup for editors - used in signup view.
        group = Group.objects.create(pk = 1, name = "Redaktoři",)
        group_permission = Permission.objects.all()[25:32]
        #give editor permission to the group
        for perm in group_permission:
            group.permissions.add(perm)
        #creates testuser (It is not created by custom sign-up view!)
        user = User.objects.create_user(pk=1, username='testuser', password='12345', is_staff = True)
        user.groups.add(group)
        #creates tag
        tag = ArticleTagModel.objects.create(
            pk= 1,
            name = "Počítače",
        )
        tag2 = ArticleTagModel.objects.create(
            pk= 2,
            name = "Zvířata",
        )
        #creates Article for test user
        article = ArticleModel.objects.create(
        pk = 1,
        title="Počítače jsou přežitek",
        text = "Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. Dlouhý text o tom, jak jsou počítače přežitek, jejich místo zabírají konzole, notebooky, mobily apod. ",
        author = User.objects.get(pk=1),
        active = True)
        #Insert tag into object (M2M)
        article.tag.add(tag, tag2)


    def test_models(self):
        article = ArticleModel.objects.get(pk=1)
        tag = ArticleTagModel.objects.get(pk=1)
        user = User.objects.get(pk=1)
        #test tag model
        self.assertTrue(tag)
        self.assertEqual(tag.name, 'Počítače')
        #test article model
        self.assertEqual(article.author.username, "testuser")
        #test tag count M2M
        self.assertEqual(article.tag.count(), 2)
        #tests auto timestamp with current datetime; newly created article is always less than 24 hours fresh.
        self.assertEqual(article.check_time(), '<span style="color:green; font-weight:bold;">mladší než 24 hodin</span>')
        #test testusers group and staff
        self.assertTrue(user.is_staff)

#class EndpointsTestCase(TestCase):

