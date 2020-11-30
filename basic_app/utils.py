from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _



def send_activation_email(request, email, code):
    context = {
        'subject': _('Profile activation'),
        'uri': request.build_absolute_uri(reverse('basic_app:activate', kwargs={'code': code})),
    }

    send_mail(email, 'activate_profile', context)

def send_activation_change_email(request, email, code):
        context = {
            'subject': _('Change email'),
            'uri': request.build_absolute_uri(reverse('basic_app:change_email_activation', kwargs={'code': code})),
        }

        send_mail(email, 'change_email', context)