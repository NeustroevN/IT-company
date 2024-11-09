from django.urls import path
from . import views
from .views import application_view
# from django.conf.urls import url
# from django.conf.urls import include, url
# from django.conf.urls import include, re_path
from django.conf.urls import include
from django.urls import re_path
# from .views import purchase_view


# app_name = 'IT_Solution'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('service/', views.service),
    path('solution/', views.solution, name='solution'),
    # path("solution-save/", views.purform),
    path("purform", views.purform),
    path('application/', application_view, name='application'),
    path('appform', views.appform),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('accounts/logout/', views.logoutUser, name="logout"),


    re_path(r'^create/$', views.order_create, name='order_create'),
    # re_path(r'^orders/', include('orders.urls', namespace='orders')),

    # path('', views.product_list, name='product_list'),
    path('add/<int:solution_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove/<int:solution_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('count_cart_solution', views.count_cart_solution, name='count_cart_solution'),

     
]

