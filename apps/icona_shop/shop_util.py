from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from mezzanine.conf import settings


def send_email(to, subject, msg_mail):
    to = [to]
    from_mail = settings.DEFAULT_FROM_EMAIL


    msg = EmailMessage(subject, msg_mail, to=to, from_email=from_mail, headers = {'Reply-To': from_mail})
    msg.content_subtype = 'html'  # Main content is now text/html
    msg.send()