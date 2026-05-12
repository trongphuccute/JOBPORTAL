import threading
import logging
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

logger = logging.getLogger(_name_)


def send_employer_approved_email(user):
    try:
        site_url = getattr(settings, 'SITE_URL', 'https://jobportal-4z3o.onrender.com')

        html_content = f"""
        <div style="font-family:Arial;padding:20px;line-height:1.6">
            <h2 style="color:#2c3e50;">🎉 Xin chào {user.username},</h2>

            <p>Tài khoản của bạn đã <b>được duyệt</b>.</p>

            <p>
                Bạn có thể truy cập hệ thống tại:
            </p>

            <a href="{site_url}" 
               style="display:inline-block;padding:10px 15px;background:#4CAF50;color:white;text-decoration:none;border-radius:6px;">
               🚀 Truy cập hệ thống
            </a>

            <br><br>

            <small style="color:#888">
                Nếu bạn không yêu cầu email này, hãy bỏ qua.
            </small>
        </div>
        """

        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=user.email,
            subject="🎉 Bạn đã trở thành Employer!",
            html_content=html_content
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