from django.contrib import admin
from django.contrib import messages

from .models import EmployerRequest, User, Profile
from .utils import send_employer_approved_email_async

from jobs.models import Company


admin.site.register(User)
admin.site.register(Profile)


@admin.register(EmployerRequest)
class EmployerRequestAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'company_name',
        'status',
    )

    list_filter = (
        'status',
    )

    actions = [
        'approve_employers'
    ]

    def approve_employers(self, request, queryset):

        approved_count = 0

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

                approved_count += 1

            except Exception as e:

                print("APPROVE ERROR:", e)

        self.message_user(
            request,
            f"{approved_count} employer(s) approved successfully.",
            messages.SUCCESS
        )

    approve_employers.short_description = (
        "✅ Approve selected employers"
    )