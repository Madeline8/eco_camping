from django.contrib import admin
from .models import Contact, NewsletterSubscription


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = (
        'full_name', 'email', 'subject', 'message'
    )


class SubscriptionAdmin(admin.ModelAdmin):
    model = NewsletterSubscription
    list_display = (
        'email',
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsletterSubscription, SubscriptionAdmin)
