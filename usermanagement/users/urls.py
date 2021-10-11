from django.urls import path
from . import views
urlpatterns=[
path('',views.about,name='about'),
   path('signup/',views.signup,name='signup'),
   path('login/', views.loginUser, name="login"),
   path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name="home"),
path('home/deleteUser/<id>/', views.deleteUser, name="delete"),
   path('editprofile/',views.editprofile,name='editprofile'),



  
]

