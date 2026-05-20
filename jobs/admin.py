from django.contrib import admin
from .models import Company, Job
from jobportal.admin_site import admin_site

admin_site.register(Company)
admin_site.register(Job)