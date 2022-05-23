from .forms import SubscriptionForm


def subscription_form(request):
    newsletter_form = SubscriptionForm()

    context = {
        'newsletter_form': newsletter_form,
    }

    return context