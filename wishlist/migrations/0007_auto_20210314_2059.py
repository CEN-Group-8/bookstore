# Generated by Django 3.1.5 on 2021-03-15 00:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishlist', '0006_auto_20210314_2058'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wishlist',
            new_name='Wish',
        ),
    ]
