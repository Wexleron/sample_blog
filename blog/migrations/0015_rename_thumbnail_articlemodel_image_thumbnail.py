# Generated by Django 4.1.1 on 2022-09-26 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_articlemodel_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlemodel',
            old_name='thumbnail',
            new_name='image_thumbnail',
        ),
    ]