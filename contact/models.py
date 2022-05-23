from django.db import models


class Contact(models.Model):
    """Model to send a message and log it in the database"""
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject