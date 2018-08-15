# this file is used to convert the data from the database into the JSON format
from rest_framework import serializers
from subscriptions import models


class WebsitesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Websites
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Feedback
class SaveArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.SaveArticles
class ReadArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.ReadArticles