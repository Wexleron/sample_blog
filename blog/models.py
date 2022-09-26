from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta #Python Native library datetime library
from django.utils import timezone   #Aware datetime (Aware=With respect to TimeZone "TZ")
### START for image to thumbnail processing imports ###
from PIL import Image
from io import BytesIO
from sys import getsizeof
from django.utils.crypto import get_random_string
from django.core.files.uploadedfile import InMemoryUploadedFile
### END for image to thumbnail processing imports ###

class ArticleTagModel(models.Model):
    name = models.CharField(max_length=50, verbose_name = "Název kategorie")
    
    class Meta:
        ordering = ['-name']
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorie"
    def __str__(self):
        return f'{self.name}'

class ArticleModel(models.Model):

    # filepath for Images
    def image_directory_path(instance, filename):
        return f'Authors/{instance.author.id}/{filename}'
    # filepath for Thumbnails
    def thumbnail_directory_path(instance, filename):
        return f'Authors/{instance.author.id}/Thumbnail/{filename}'

    title = models.CharField(max_length=200,  verbose_name = "Titulek")
    text = models.TextField(max_length=18000,  verbose_name = "Text článku")  #length == 10 A4 of standard chars count (A4 = 1800 chars as per standard)
    tag = models.ManyToManyField(ArticleTagModel, related_name="articles", help_text="Vyber 1 či více kategorií, v které se má čánek zobrazovat", verbose_name = "Kategorie")
    image = models.ImageField(upload_to = image_directory_path, default='global/img/build.png',  verbose_name = "Obrázek")
    image_thumbnail=models.ImageField(upload_to = thumbnail_directory_path, default='global/img/build_thumbnail.png', verbose_name = "Mini-obrázek")
    created = models.DateTimeField(auto_now=True, editable=False,)
    author = models.ForeignKey(get_user_model(), editable=False, null=True, on_delete=models.PROTECT,)  #TO-DO - PROTECT exception should be proccessed in view !
    active = models.BooleanField(default=False, help_text="Zaškrtnutím bude článek publikovaný. Publikaci lze v budoucnu zrušit", verbose_name = "Publikovat ?")

    class Meta:
        ordering = ['-created']
        verbose_name = "Článek"
        verbose_name_plural = "Články"
    
    #Function to check image and create thumbnail
    def save(self, **kwargs):
        # Opening the uploaded image
        try:
            kwargs['force_insert'] = True
            received_image = Image.open(self.image)
            #Creating 2 empty vars for binary data
            output_thumbnail = BytesIO()
            output_image = BytesIO()
            image_to_thumbnail = Image.open(self.image)
            #Check size, and output resized thumbnail
            if image_to_thumbnail.height > 50 or image_to_thumbnail.width > 50:
                thumbnail_output_size = (50, 50)
                image_to_thumbnail.thumbnail(thumbnail_output_size)
                image_to_thumbnail.save(output_thumbnail,format='PNG',quality=100)
            # Resize/modify the image
            received_image = received_image.resize((300, 300))
            # after modifications, save it to the output
            received_image.save(output_image, format='PNG', quality=100)
            output_thumbnail.seek(0)
            unique_id = get_random_string(length=32)
            # change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output_image,
                                'ImageField', "%s.png" %
                               self.image.name.split('.')[0],
                               'image/png',
                                getsizeof(output_image), None)
            self.image_thumbnail = InMemoryUploadedFile(output_thumbnail,
                                'ImageField',"%s.png" % unique_id,
                                'image/png',
                                 getsizeof(output_thumbnail), None)
            super(ArticleModel, self).save()
        except:
            super(ArticleModel, self).save()
    
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