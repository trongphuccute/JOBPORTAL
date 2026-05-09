from django.urls import path
from . import views
 
app_name = 'applications'

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('save/<int:job_id>/', views.save_job, name='save_job'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('job/<int:job_id>/applicants/', views.applicants_list, name='applicants'),
    path('update-status/<int:app_id>/<str:status>/', views.update_application_status, name='update_status'),
    path('update-status-employer/<int:app_id>/<str:status>/', views.update_status, name='update_status_employer'),
] 