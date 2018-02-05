from django.urls import path
from . import views
urlpatterns = [
    # basic urls
    path('',views.HomePageView,name='home'),
    path('about/',views.AboutPageView.as_view(),name='about'),
    path('feedback/',views.FeedbackPageView,name='feedback'),

    # Signup url
    path('signup/',views.SignUp.as_view(),name='signup'),

    # core urls
    path('list/', views.SubsListView.as_view(), name='list'),
    path('add/', views.addSubs, name='add'),
    path('contact/', views.ContactPageView, name='contact'),
    path('reader/<path:l>/', views.ReaderModeView, name='reader'),
    path('delete/<int:pk>', views.SubsDeleteView.as_view(), name='delete'),
    
]
