from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('about/',views.AboutPageView.as_view(),name='about'),
    path('feedback/',views.FeedbackPageView.as_view(),name='feedback'),
    path('signup/',views.SignUp.as_view(),name='signup'),
]
