from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.urls import path

from jobs.models import Job
from accounts.models import User
from applications.models import Application


class JobPortalAdminSite(AdminSite):

    site_header = "Job Portal Admin"

    site_title = "Job Portal"

    index_title = "Dashboard"

    def get_urls(self):

        urls = super().get_urls()

        custom_urls = [

            path(
                "analytics/",
                self.admin_view(self.analytics_view),
                name="analytics",
            ),

        ]

        return custom_urls + urls

    def analytics_view(self, request):

        context = dict(

            self.each_context(request),

            total_jobs=Job.objects.count(),

            total_users=User.objects.count(),

            total_applications=Application.objects.count(),
        )

        return TemplateResponse(
            request,
            "admin/analytics.html",
            context
        )


admin_site = JobPortalAdminSite(name="jobportal_admin")