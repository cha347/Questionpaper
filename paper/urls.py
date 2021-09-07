from django.contrib import admin
from django.urls import path,include
from .import views
from paper.views import *



urlpatterns = [
   
    path('',views.homepage),
    path('search/',views.detail),
    path('welcome.html',views.welcome,name="welcome"),
    path('index.html', views.index,name='index'),
    path('load-courses/',load_courses,name='ajax_load_courses'),
    path('fillsem.html',views.HomeView.as_view(),name='papers/semester'),
    path('search_data',views.search_data.as_view(),name='search_data'),
    path('multiple_details',views.search_detail),
    path('searchinformation.html',views.SearchInfo),
   path('downloadpdf//', views.download_pdf_file, name='download_pdf_file'),
  path('signup.html/',views.signup),
  path('login.html/',views.user_login),
  path('admin_login.html/',views.admin_login),
 path('admin_homepage.html/',views.admin_home),
 path('logout/',views.logout_admin,name="admin_logout"),
 path('LOGOUT/',views.logout),
 path('user_home/',views.user_home),
 path('about.html/',views.about),
  path('contact.html/',views.formdetails),
 

]