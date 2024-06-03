from django.urls import path
# from .views import geeks_view
from .views import index
from . import views
from django.contrib.auth import views as auth_views 
from .views import application_view

urlpatterns = [
    # path('', index),
    path('', views.index, name = 'index'),
    path('index/', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('service/', views.service),
    path('solution/', views.solution),
    path("solution-save/", views.purform),
    # path('application/', views.application),
    path('application/', application_view, name='application'),
    
    path('appform', views.appform),
    # path('', views.index, name = 'index'),
    path("signup/", views.SignUp.as_view(), name="signup"),

    # path('logout/', views.logoutUser, name="logout"),
    path('accounts/logout/', views.logoutUser, name="logout"),
    # path('', geeks_view),

]