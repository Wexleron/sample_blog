from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta #Python Native library datetime library
from django.utils import timezone   #Aware datetime (Aware=With respect to TimeZone "TZ")

class ArticleTagModel(models.Model):
    name = models.CharField(max_length=50, verbose_name = "Název kategorie")
    
    class Meta:
        ordering = ['-name']
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorie"
    def __str__(self):
        return f'{self.name}'

class ArticleModel(models.Model):

    # filepath for media files in function.
    def author_directory_path(instance, filename):
        return f'Authors/{instance.author.id}/{filename}'

    title = models.CharField(max_length=200,  verbose_name = "Titulek")
    text = models.TextField(max_length=18000,  verbose_name = "Text článku")  #length == 10 A4 of standard chars count (A4 = 1800 chars as per standard)
    tag = models.ManyToManyField(ArticleTagModel, related_name="articles", help_text="Vyber 1 či více kategorií, v které se má čánek zobrazovat", verbose_name = "Kategorie")
    image = models.ImageField(upload_to = author_directory_path, default='global/img/build.png',  verbose_name = "Obrázek")
    created = models.DateTimeField(auto_now=True, editable=False,)
    author = models.ForeignKey(get_user_model(), editable=False, null=True, on_delete=models.PROTECT,)  #TO-DO - PROTECT exception should be proccessed in view !
    active = models.BooleanField(default=False, help_text="Zaškrtnutím bude článek publikovaný. Publikaci lze v budoucnu zrušit", verbose_name = "Publikovat ?")

    class Meta:
        ordering = ['-created']
        verbose_name = "Článek"
        verbose_name_plural = "Články"
    
    #String for article model based on if article is published or not
    def __str__(self):
        self.date = self.created.strftime('%d.%m.%Y')   #datetime format to pretty string
        if self.active:
            return f'PUBLIKOVÁN | Titulek: {self.title} | Vytvořen: {self.date}'
        else:
            return f'NEPUBLIKOVÁN | Titulek: {self.title} | Vytvořen: {self.date}'

    #function to chesk if article is older than 24 hours or not
    def check_time(self):
        self.now = timezone.now()   #Initialize Aware datetime
        if self.created > self.now - timedelta(hours=24):
            return '<span style="color:green; font-weight:bold;">mladší než 24 hodin</span>' 
        else:
            return '<span style="color:orange; font-weight:bold;">starší více jak 24 hodin</span>'