from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request-employer/', views.request_employer, name='request_employer'),
    path ('', views.home, name='home'),
    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path ('profile/', views.profile, name='profile'),
]