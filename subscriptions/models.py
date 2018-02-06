from django.db import models
from django.urls import reverse
# Create your models here.


class Websites(models.Model):
    app_user=models.CharField(max_length=200,default='')
    web_name = models.CharField(max_length=200)
    web_url = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.web_name

class Feedback(models.Model):
    to_user=models.CharField(max_length=200)
    from_user=models.CharField(max_length=200)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.from_user+':-'+self.message[:50]

class SaveArticles(models.Model):
    app_user=models.CharField(max_length=200)
    article_link=models.CharField(max_length=300)

    def __str__(self):
        return self.app_user+'-'+self.article_link