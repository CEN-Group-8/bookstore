# Generated by Django 3.1.5 on 2021-03-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bookstore_api', '0002_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='cart',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='saveLater',
            field=models.JSONField(null=True),
        ),
    ]
