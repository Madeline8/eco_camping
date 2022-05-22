from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = (
        'full_name', 'email', 'subject', 'message'
    )

    ordering = ('full_name',)

admin.site.register(Contact, ContactAdmin)