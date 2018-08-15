# ___________________REST FRAMEWORK CODE HERE__________________
# posts/views.py
from django.shortcuts import render
from rest_framework import generics
from subscriptions.models import Websites,SaveArticles,ReadArticles,Feedback
from .serializers import WebsitesSerializer,FeedbackSerializer,SaveArticleSerializer,ReadArticlesSerializer
# from django.contrib.auth.mixins import LoginRequiredMixin

def APIHomePage(request):
    return render(request,"api.html")

class WebsitesList(generics.ListCreateAPIView):
    queryset = Websites.objects.all()
    serializer_class = WebsitesSerializer

class SaveArticlesList(generics.ListCreateAPIView):
    queryset = SaveArticles.objects.all()
    serializer_class = SaveArticleSerializer

class ReadArticlesList(generics.ListCreateAPIView):
    queryset = ReadArticles.objects.all()
    serializer_class = ReadArticlesSerializer

class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
