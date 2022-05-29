from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def policies(request):
    """
    A view to return the company policies
    """
    return render(request, 'home/policies.html')
