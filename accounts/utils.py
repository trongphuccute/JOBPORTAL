from django.core.mail import send_mail
from django.conf import settings
import logging
import threading

logger = logging.getLogger(__name__)

def send_employer_approved_email_async(user):
    threading.Thread(target=send_employer_approved_email_async, args=(user,)).start()
    try:
        subject = "🎉 Bạn đã trở thành Employer!"

        site_url = getattr(settings, 'SITE_URL', 'https://jobportal-4z3o.onrender.com')

        message = f"""
Xin chào {user.username},

Chúc mừng! Tài khoản của bạn đã được duyệt.

Truy cập:
{site_url}/
"""

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        logger.info(f"Email sent to {user.email}")

    except Exception as e:
        logger.exception(f"Email error for {user.email}: {e}")