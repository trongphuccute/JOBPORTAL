from django.contrib import admin
from .models import EmployerRequest, User, Profile, Company
from .utils import send_employer_approved_email


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
                }
            )

            # 🔥 GỬI EMAIL
            send_employer_approved_email(user)