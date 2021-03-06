from django import forms
from .models import Contact, NewsletterSubscription


class ContactForm(forms.ModelForm):
    """
    Form for anyone (also non-users) to contact EcoCamping
    """
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }

        for field in self.fields:
            # Remove labels and leave placeholders only
            self.fields[field].label = False
            # Adds a asterisk to fields that are required
            placeholder = f'{placeholders[field]} *'
            # Placeholder will be the same as the value in the dict above
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Set css
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'


class SubscriptionForm(forms.ModelForm):
    """
    Create a form for users to subscribe to newsletters
    """

    class Meta:
        model = NewsletterSubscription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs['class'] = "subscribe-input"
        self.fields["email"].label = False
        self.fields["email"].widget.attrs["placeholder"] = "Email *"
