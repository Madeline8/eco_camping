from django.shortcuts import render


def contact(request):
    """ A view that renders the contact page contents """
    
    return render(request, 'contact/contact.html')
