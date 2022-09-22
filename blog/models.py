from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta #Python Native library datetime library
from django.utils import timezone   #Aware datetime (Aware=With respect to TimeZone "TZ")

class ArticleTagModel(models.Model):
    name = models.CharField(max_length=50,)
    
    class Meta:
        ordering = ['-name']
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorie"
    def __str__(self):
        return f'{self.name}'

class ArticleModel(models.Model):

    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    def author_directory_path(instance, filename):
        return f'author_{instance.user.id}/{filename}'

    title = models.CharField(max_length=200,)
    text = models.TextField(max_length=18000,)  #length == 10 A4 of standard chars count (A4 = 1800 chars as per standard)
    tag = models.ManyToManyField(ArticleTagModel, related_name="articles",)
    image = models.ImageField(upload_to = author_directory_path, default='global/img/build.png',)
    created = models.DateTimeField(auto_now=True, editable=False,)
    author = models.ForeignKey(get_user_model(), editable=False, null=True, on_delete=models.PROTECT,)  #TO-DO - PROTECT exception should be proccessed in view !
    active = models.BooleanField(default=False,)

    class Meta:
        ordering = ['-created']
        verbose_name = "Článek"
        verbose_name_plural = "Články"
    
    def __str__(self):
        self.date = self.created.strftime('%d.%m.%Y')   #datetime format to pretty string
        if self.active:
            return f'PUBLIKOVÁN | Článek: {self.title} | Vytvořen: {self.date}'
        else:
            return f'NEPUBLIKOVÁN | Článek: {self.title} | Vytvořen: {self.date}'



""" REWORK
    def check_time(self):
        self.now = timezone.now()   #Initialize Aware datetime
        if self.created > self.now - timedelta(hours=3):
            return "< 3 hodiny" 
        elif self.created  > self.now - timedelta(hours=8):
            return "3 - 8 hodinami"
        elif self.created  > self.now - timedelta(hours=24):
            return "8 - 24 hodinami"
        elif self.created > self.now - timedelta(hours=72):
            return " 24 - 72 hodinami"
        else:
            return "Informace o prodejci nemusí být pravdivá"
            """