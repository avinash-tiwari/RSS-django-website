from django.urls import path
from . import views
urlpatterns = [
    path('', views.APIHomePage,name="API_home"),
    path('subs/', views.WebsitesList.as_view()),
    path('save/', views.SaveArticlesList.as_view()),
    path('read/', views.ReadArticlesList.as_view()),
    path('feedback/', views.FeedbackList.as_view()),
]
