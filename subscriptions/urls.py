from django.urls import path
from . import views
urlpatterns = [
    # basic urls
    path('',views.HomePageView.as_view(),name='home'),
    path('about/',views.AboutPageView.as_view(),name='about'),
    path('feedback/',views.FeedbackPageView.as_view(),name='feedback'),

    # Signup url
    path('signup/',views.SignUp.as_view(),name='signup'),

    # core urls
    path('list/', views.SubsListView.as_view(), name='list'),
    path('add/', views.AddCreateView.as_view(), name='add'),
    path('delete/<int:pk>', views.SubsDeleteView.as_view(), name='delete'),

]
