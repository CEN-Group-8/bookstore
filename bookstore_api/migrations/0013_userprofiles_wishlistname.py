# Generated by Django 3.1.5 on 2021-03-29 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_api', '0012_auto_20210328_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='wishlistName',
            field=models.JSONField(null=True),
        ),
    ]