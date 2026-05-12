from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_employer_approved_email(user):
    subject = "🎉 Bạn đã trở thành Employer!"
    
    # Get site domain from settings or use default
    site_url = getattr(settings, 'SITE_URL', 'https://jobportal-4z3o.onrender.com')

    message = f"""
Xin chào {user.username},

Chúc mừng! Tài khoản của bạn đã được duyệt thành Nhà tuyển dụng.

Bạn có thể đăng job và quản lý ứng viên ngay bây giờ.

Truy cập hệ thống:
{site_url}/

JobPortal Team
"""

    try:
        # Check if email is configured
        if not settings.DEFAULT_FROM_EMAIL or settings.DEFAULT_FROM_EMAIL == 'None':
            logger.warning(f"⚠️  Email not configured, skipping email to {user.email}")
            return
            
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=True,  # Don't crash if email fails
        )
        logger.info(f"✅ Email sent successfully to {user.email}")
    except Exception as e:
        # Log error but don't raise - approval should not fail due to email
        logger.error(f"❌ Failed to send email to {user.email}: {str(e)}")