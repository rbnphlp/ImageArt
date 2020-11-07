from django.shortcuts import render

# Create your views here.
from .models import Painting

# Create your views here.

def all_paintings(request):
    """ A view to show all paintings, including sorting and search queries """

    paintings = Painting.objects.all()

    context = {
        'paintings': paintings,
    }

    return render(request, 'Gallery/gallery.html', context)