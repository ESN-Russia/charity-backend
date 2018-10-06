import os
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context


SENDERS = {
    "charity": {
        "user": "charity@esnrussia.org",
        "password": os.getenv("EMAIL_PASSWORD_CHARITY"),
        "from": "ESN Charity <charity@esnrussia.org>"
    },
}
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
print("TEMPLATE_DIR", TEMPLATE_DIR)

def send_message(recipient, title, body, sender="charity"):
    print("[MAIL] Sending mail '" + title + "' to '" + recipient + "'")
    send_mail(
        title,
        body,
        SENDERS[sender]["from"],
        [recipient],
        fail_silently=False,
        auth_user=SENDERS[sender]["user"],
        auth_password=SENDERS[sender]["password"],
        html_message=body
    )
    print("[MAIL] Sent ### '" + title + "' to '" + recipient + "'")


def render_message(template_name, **kwargs):
    print("Rendering template", os.path.join(TEMPLATE_DIR,template_name))
    return get_template( os.path.join(TEMPLATE_DIR,template_name) ).render(kwargs)
