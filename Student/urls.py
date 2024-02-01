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
    path('admin/', admin.site.urls),
    path("",views.Home),
    path("enqry/",views.enqry),
    path("login_student/",views.login_student),
    path("login_student/student_profile/<int:key>/", views.student_profile, name="student_profile"),
    path('student_info/<int:key>/', views.student_info, name='student_info'),
    path('student_info/student_classmates/<int:key>/', views.student_classmates, name='student_classmates'),
    path('student_info/student_classmates/chats<int:key>/<int:rkey>', views.student_chats, name='student_chats'),
    path("delete_entry/<int:key>/<int:rkey>/<int:msgid>",views.delete_entry,name="delete_entry"),
    path('student_attendence/<int:key>/', views.student_attendence, name='student_attendence'),
    path('student_marks/<int:key>/', views.student_marks, name='student_marks'),
    path('student_course/<int:key>/', views.student_course, name='student_course'),
    path('Student_learning/<int:key>/', views.Student_learning, name='Student_learning'),
    path('Student_examform/<int:key>/', views.Student_examform, name='Student_examform'),
    path('ask_teacher/<int:key>/', views.ask_teacher, name='ask_teacher'),


]
 
