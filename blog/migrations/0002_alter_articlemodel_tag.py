# Generated by Django 4.1.1 on 2022-09-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='tag',
            field=models.ManyToManyField(related_name='articles', to='blog.articletagmodel'),
        ),
    ]
