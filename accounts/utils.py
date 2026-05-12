from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_employer_approved_email(user):
    """Send approval email - non-blocking, email is optional"""
    subject = "🎉 Bạn đã trở thành Employer!"
    
    # Get site domain from settings
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
        if not settings.DEFAULT_FROM_EMAIL or settings.DEFAULT_FROM_EMAIL in ['None', None, '']:
            logger.warning(f"⚠️  Email not configured, skipping email to {user.email}")
            return
        
        # Try to send email with timeout
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=True,
            timeout=5  # 5 second timeout
        )
        logger.info(f"✅ Email sent to {user.email}")
        
    except Exception as e:
        # Just log error, don't crash
        logger.error(f"Email error for {user.email}: {str(e)}")