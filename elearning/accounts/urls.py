from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about),
    path('contact/', views.contact),
    path('courses/', views.courses),
    path('login/', views.loginpage, name="login"),
    path('register/', views.registerpage, name="register"),

    
]