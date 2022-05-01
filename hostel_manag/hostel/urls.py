"""hostel_manag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_user,name="login-page"),
    path('home/',views.home,name="home-page"),
    path('registration/',views.student_registration,name="student_registration"),
    path('visitordetails/',views.visitor_registration,name="visitor_registration"),
    path('facilities/',views.facilities,name="facilities"),
    path('profile/',views.profile,name="profile"),
    path('contact_save/',views.saveContactDetails,name="contact_save"),
    path('visitor_save/',views.saveVisitorDetails,name="visitor_save"),
    path('student_save/',views.saveStudentDetails,name="student_save"),
    path('about_us/',views.aboutUs,name="about_us"),
]
