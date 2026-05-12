from django.contrib import admin
from django.contrib import messages
from .models import EmployerRequest, User, Profile
from .utils import send_employer_approved_email
from jobs.models import Company


admin.site.register(User)
admin.site.register(Profile)


@admin.register(EmployerRequest)
class EmployerRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'status')
    actions = ['approve']

    def approve(self, request, queryset):
        for req in queryset:
            req.status = 'approved'
            req.save()

            user = req.user
            user.role = 'employer'
            user.save()

            # 🔥 TẠO COMPANY (PHẦN BẠN ĐANG THIẾU)
            Company.objects.get_or_create(
                user=user,
                defaults={
                    "name": req.company_name,
                    "location": req.company_location,
                    "website": req.company_website,
                    "description": req.company_description
                }
            )

            # 🔥 GỬI EMAIL
            send_employer_approved_email(user)
        
        messages.success(request, f"✅ {queryset.count()} employer(s) approved successfully!")