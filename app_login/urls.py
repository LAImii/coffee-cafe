from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register_complete', views.register_complete, name='register_complete'),
    path('logout', views.logout, name='logout'),
]