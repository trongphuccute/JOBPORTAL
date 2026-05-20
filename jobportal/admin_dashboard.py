from django.contrib import admin
from django.contrib.auth import get_user_model

from jobs.models import Job
from applications.models import Application

User = get_user_model()

admin.site.index_template = "admin/index.html"

original_index = admin.site.index


def custom_index(request, extra_context=None):

    extra_context = extra_context or {}

    extra_context["total_jobs"] = (
        Job.objects.count()
    )

    extra_context["total_users"] = (
        User.objects.count()
    )

    extra_context["total_applications"] = (
        Application.objects.count()
    )

    extra_context["total_employers"] = (
        User.objects.filter(
            is_employer=True
        ).count()
    )

    return original_index(
        request,
        extra_context=extra_context
    )


admin.site.index = custom_index