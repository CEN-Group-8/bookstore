# Generated by Django 3.1.5 on 2021-03-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0011_auto_20210328_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='wishlist',
            field=models.JSONField(null=True),
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]