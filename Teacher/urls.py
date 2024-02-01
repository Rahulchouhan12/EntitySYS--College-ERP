"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("login_Teacher/",views.login_Teacher),
    path("login_Teacher/Teacher_profile/<int:key>/", views.Teacher_profile, name="Teacher_profile"),
    path('Teacher_info/<int:key>/', views.Teacher_info, name='Teacher_info'),
    path('Teacher_Attendence/<int:key>/', views.Teacher_Attendence, name='Teacher_Attendence'),
    path('Teacher_Grading/<int:key>/', views.Teacher_Grading, name='Teacher_Grading'),
    path('Teacher_Annoncement/<int:key>/', views.Teacher_Annoncement, name='Teacher_Annoncement'),
]
 
