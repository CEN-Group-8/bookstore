# Generated by Django 3.1.5 on 2021-03-08 23:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0004_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
