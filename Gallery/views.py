from django.shortcuts import render, get_object_or_404

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




def product_detail(request, painting_id):
    """ A view to show individual product/painting details """

    product = get_object_or_404(Painting, pk=painting_id)

    context = {
        'product': product,
    }

    return render(request, 'Gallery/product_detail.html', context)








