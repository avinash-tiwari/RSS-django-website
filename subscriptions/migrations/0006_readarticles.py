# Generated by Django 2.0.3 on 2018-05-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_savearticles_article_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_user', models.CharField(max_length=200)),
                ('article_link', models.CharField(max_length=300)),
                ('article_title', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
