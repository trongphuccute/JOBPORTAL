from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),        
    path('<int:id>/', views.job_detail, name='job_detail'),  
    path('create/', views.create_job, name='create_job'),
    path('my-jobs/', views.my_jobs, name='my_jobs'),
    path('edit/<int:id>/', views.edit_job, name='edit_job'),
    path('delete/<int:id>/', views.delete_job, name='delete_job'),
    path('company/<int:id>/', views.company_profile, name='company_profile'),
    path('', views.home, name='home'),
]