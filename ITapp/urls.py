from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from .views import application_view

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('service/', views.service),
    path('solution/', views.solution),
    path("solution-save/", views.purform),
    path('application/', application_view, name='application'),
    path('appform', views.appform),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('accounts/logout/', views.logoutUser, name="logout"),
]