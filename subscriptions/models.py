from django.db import models
from django.urls import reverse
# Create your models here.


class Websites(models.Model):
    # app_user=models.ForeignKey('auth.User',on_delete=models.CASCADE,default='')
    web_name = models.CharField(max_length=200)
    web_url = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.web_name

    def get_absolute_url(self):
        return reverse('home')
