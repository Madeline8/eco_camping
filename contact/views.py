from django.shortcuts import render, redirect
from .models import Contact, NewsletterSubscription
from .forms import ContactForm, SubscriptionForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string


def contact(request):
    """
   A view that renders the contact page contents
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            form.save()
            messages.success(
                request,
                f'Thank you for your message, {full_name}!'
            )
            # Email to the sender confirming the message
            data = form.save()
            subject = render_to_string(
                'contact/message_templates/subject.txt',
                {'data': data}
            )
            body = render_to_string(
                'contact/message_templates/message_body.txt',
                {'data': data}
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )
        else:
            messages.error(
                request,
                "Your message could not be sent, please make sure all fields are entered and valid."
            )

    form = ContactForm()

    context = {
        'form': form,
        'on_contact_page': True
    }
    return render(request, 'contact/contact.html', context)


def newsletter_subscribe(request):
    """
    View to subscribe to a newsletter. 
    """
    url = request.META.get('HTTP_REFERER')
    newsletter_form = SubscriptionForm(request.POST)
    if newsletter_form.is_valid():
        newsletter_form.save()
        messages.success(
            request,
            "Thank you! You have now subscribed to our newsletter. Email confirmation has been sent to you. "
            )

        # Confirm the user has been suscribed via email
        data = newsletter_form.save()
        subscriber_email_address = data.email
        subject = render_to_string(
            'contact/message_templates/'
            'subscribe_subject.txt',
        )
        body = render_to_string(
            'contact/message_templates/'
            'subscribe_body.txt',
            {'data': data}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber_email_address],
        )
        return HttpResponseRedirect(url)
    else:
        messages.error(
            request,
            "Ops, something has gone wrong. Please make sure the email address is correct."
        )
        return HttpResponseRedirect(url)

