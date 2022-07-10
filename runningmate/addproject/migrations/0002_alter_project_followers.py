# Generated by Django 4.0.5 on 2022-07-10 14:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('addproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='followers',
            field=models.ManyToManyField(related_name='followers', through='addproject.Follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
