# Generated by Django 2.2.1 on 2019-05-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, verbose_name='PK')),
                ('title', models.TextField(verbose_name='title')),
                ('article', models.TextField(verbose_name='article with markdown format')),
                ('author', models.CharField(max_length=64, verbose_name='author')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='date of create')),
                ('update_date', models.DateTimeField(auto_now_add=True, verbose_name='date of last modify')),
            ],
        ),
    ]
