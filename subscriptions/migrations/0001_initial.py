# Generated by Django 2.0.2 on 2018-02-02 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Websites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_name', models.CharField(max_length=200)),
                ('web_url', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
