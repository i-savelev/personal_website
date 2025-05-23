# Generated by Django 5.2 on 2025-05-08 08:23

import django.utils.timezone
import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_title', models.CharField(max_length=250, unique=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', markdownx.models.MarkdownxField()),
                ('content', markdownx.models.MarkdownxField(blank=True)),
                ('pub', models.BooleanField()),
                ('tags', models.ManyToManyField(blank=True, related_name='articles', to='blog.tag')),
            ],
        ),
    ]
