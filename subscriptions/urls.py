from django.urls import path
from . import views
urlpatterns = [
    # basic urls
    path('',views.HomePageView,name='home'),#home page url
    path('about/',views.AboutPageView.as_view(),name='about'),#about page url
    path('feedback/',views.FeedbackPageView,name='feedback'),#feedback page url
    # Signup url
    path('signup/',views.SignUp.as_view(),name='signup'),#signup page url

    # core urls
    path('list/', views.SubsListView.as_view(), name='list'),#list page url
    path('add/', views.addSubs, name='add'),#new subscriptions addition page
    path('reader/<path:l>/', views.ReaderModeView, name='reader'),#reader mode url it will give the article url
    path('save/<path:l>/<path:n>', views.SaveArticleView, name='save'),#save page url
    path('savepage/', views.SavePageView, name='savepage'),#list all the saved pages
    path('delete/<int:pk>', views.SubsDeleteView.as_view(), name='delete'),#delete subscriptions
    path('remove/<path:l>', views.SaveRemove, name='remove_save'),#remove the saved article
    
]
