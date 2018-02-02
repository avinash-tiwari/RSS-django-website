from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'

class FeedbackPageView(TemplateView):
    template_name='feedback.html'

class SignUp(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')    
    template_name='signup.html'