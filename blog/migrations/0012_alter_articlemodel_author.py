# Generated by Django 4.1.1 on 2022-09-24 09:57

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_alter_articlemodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='author',
            field=models.ForeignKey(default=django.contrib.auth.models.User, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
