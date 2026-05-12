from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_employer_approved_email(user):
    subject = "🎉 Bạn đã trở thành Employer!"
    
    # Get site domain from settings or use default
    site_url = getattr(settings, 'SITE_URL', 'https://jobportal.onrender.com')

    message = f"""
Xin chào {user.username},

Chúc mừng! Tài khoản của bạn đã được duyệt thành Nhà tuyển dụng.

Bạn có thể đăng job và quản lý ứng viên ngay bây giờ.

Truy cập hệ thống:
{site_url}/

JobPortal Team
"""

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        logger.info(f"✅ Email sent successfully to {user.email}")
    except Exception as e:
        logger.error(f"❌ Failed to send email to {user.email}: {str(e)}")
        raise