from django.shortcuts import render

from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view that renders the shopping bag contents page """

    return render(request, 'bag/bag.html')
