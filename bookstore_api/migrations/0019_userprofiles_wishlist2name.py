# Generated by Django 3.1.5 on 2021-04-02 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0018_userprofiles_wishlist2'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='wishlist2Name',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
