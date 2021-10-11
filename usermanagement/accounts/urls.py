from django.urls import path
from . import views
urlpatterns=[
   path('signup/',views.signup,name='register'),
   path('login/', views.loginUser, name="login"),
   path('logout/', views.logoutUser, name="logout"),

  
]

