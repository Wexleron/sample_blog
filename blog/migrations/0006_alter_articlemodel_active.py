# Generated by Django 4.1.1 on 2022-09-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_articlemodel_active_alter_articlemodel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='active',
            field=models.BooleanField(default=False, help_text='Zaškrtnutím bude článek publikovaný. Publikaci lze v budoucnu zrušit', verbose_name='Publikovat ?'),
        ),
    ]
