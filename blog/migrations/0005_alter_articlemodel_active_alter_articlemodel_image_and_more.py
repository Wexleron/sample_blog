# Generated by Django 4.1.1 on 2022-09-22 14:35

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_název článku_articlemodel_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Publikovat ?'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='image',
            field=models.ImageField(default='global/img/build.png', upload_to=blog.models.ArticleModel.image_directory_path, verbose_name='Obrázek'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='tag',
            field=models.ManyToManyField(help_text='Vyber 1 či více kategorií, v které se má čánek zobrazovat', related_name='articles', to='blog.articletagmodel', verbose_name='Kategorie'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='text',
            field=models.TextField(max_length=18000, verbose_name='Text článku'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulek'),
        ),
    ]
