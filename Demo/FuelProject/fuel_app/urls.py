from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', auth_views.LoginView.as_view(), name='login'),     #Pouria
    path('logout', auth_views.LogoutView.as_view(), name='logout'),  #Pouria
    path('register', views.register, name='register'),               #Lizzy 
    path('quote', views.quote, name='quote'),                        #Ali
    path('history', views.history, name='history'),                  #Ali
    path('profile', views.profile, name='profile')                   #Team
]