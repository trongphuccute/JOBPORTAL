from django.contrib import admin
from .models import Resume, Application, SavedJob


admin.site.register(Resume)
admin.site.register(Application)
admin.site.register(SavedJob)