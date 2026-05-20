from django.contrib import admin
from django.contrib import messages
from .models import EmployerRequest, User, Profile
from .utils import send_employer_approved_email_async
from jobs.models import Company
import threading
from jobportal.admin_site import admin_site

admin_site.register(User)
admin_site.register(Profile)


@admin.register(EmployerRequest)
class EmployerRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'status')
    actions = ['approve']

    def approve(self, request, queryset):
        for req in queryset:
            try:
                req.status = 'approved'
                req.save()

                user = req.user
                user.role = 'employer'
                user.save()

                Company.objects.get_or_create(
                    user=user,
                    defaults={
                        "name": req.company_name or "",
                        "location": req.company_location or "",
                        "website": req.company_website or "",
                        "description": req.company_description or ""
                    }
                )

                if user.email:
                    send_employer_approved_email_async(user)
                else:
                    print(f"No email for {user.username}")

            except Exception as e:
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f"Approve error: {str(e)}")

        messages.success(request, f"✅ {queryset.count()} employer(s) approved successfully!")