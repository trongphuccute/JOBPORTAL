from django.core.mail import send_mail
from django.conf import settings

def send_employer_approved_email(user):
    subject = "🎉 Bạn đã trở thành Employer!"

    message = f"""
Xin chào {user.username},

Chúc mừng! Tài khoản của bạn đã được duyệt thành Nhà tuyển dụng.

Bạn có thể đăng job và quản lý ứng viên ngay bây giờ.

Truy cập hệ thống:
http://127.0.0.1:8000/

JobPortal Team
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )