from django.contrib import admin
from .models import Resume, Application, SavedJob
from jobportal.admin_site import admin_site

admin_site.register(Resume)
admin_site.register(Application)
admin_site.register(SavedJob)