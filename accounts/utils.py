import threading
import logging

from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

logger = logging.getLogger(__name__)


def send_employer_approved_email(user):
    try:
        site_url = getattr(settings, 'SITE_URL', 'https://jobportal-4z3o.onrender.com')

        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=user.email,
            subject="🎉 Bạn đã trở thành Employer!",
            plain_text_content=f"""
Xin chào {user.username},

Tài khoản của bạn đã được duyệt.

Truy cập:
{site_url}/
"""
        )

        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)

        logger.info(f"SendGrid status: {response.status_code}")

    except Exception as e:
        logger.exception(f"SendGrid error: {e}")


def send_employer_approved_email_async(user):
    thread = threading.Thread(
        target=send_employer_approved_email,
        args=(user,)
    )
    thread.start()