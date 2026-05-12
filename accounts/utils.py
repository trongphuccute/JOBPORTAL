from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_employer_approved_email(user):
    subject = "🎉 Bạn đã trở thành Employer!"

    site_url = getattr(settings, 'SITE_URL', 'https://jobportal-4z3o.onrender.com')

    message = f"""
Xin chào {user.username},

Chúc mừng! Tài khoản của bạn đã được duyệt.

Truy cập:
{site_url}/
"""

    try:
        if not settings.EMAIL_HOST_USER or not settings.EMAIL_HOST_PASSWORD:
            logger.warning("Email not configured")
            return

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=True,
        )

        logger.info(f"Email sent to {user.email}")

    except Exception:
        logger.exception(f"Email error for {user.email}")