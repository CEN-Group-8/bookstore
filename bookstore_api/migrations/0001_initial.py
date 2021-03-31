# Generated by Django 3.1.5 on 2021-02-25 01:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.IntegerField()),
                ('pageCount', models.IntegerField()),
                ('publishedDate', models.JSONField()),
                ('thumbnailUrl', models.URLField()),
                ('shortDescription', models.CharField(max_length=1000)),
                ('longDescription', models.CharField(max_length=3000)),
                ('status', models.CharField(max_length=100)),
                ('authors', models.JSONField()),
                ('categories', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('emailAddress', models.CharField(max_length=100)),
                ('homeAddress', models.CharField(max_length=100)),
            ],
        ),
    ]
