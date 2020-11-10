from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Painting
from .forms import PaintingForm
from utils.style_transfer import * 
# Create your views here.

"dimesnions for painting"
new_width  = 380
new_height = 512



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






def add_painting(request):
    """ Add a product to the store """
    form = PaintingForm()
    template = 'Gallery/add_painting.html'
    template2 = 'Gallery/painting_no_gallery.html'

    "if add to gallery is not checked , simply process the images and output to html , else  save each image  and generate a different template" 
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        print("In request post")
        if form.is_valid():
            "check if add to gallery is not added  and simply render no saving images"
            add_to_gallery=form.cleaned_data['Add_to_Gallery']
            print(add_to_gallery)
            if not add_to_gallery :
                 " process the  files  and render "
                 
                 upload_pic=form.cleaned_data['upload_pic']
                 upload_image = PIL.Image.open(upload_pic)
                 style_pic=form.cleaned_data['style_pic']
                 style_image = PIL.Image.open(style_pic)
                 
                 hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
                 l=load_img(upload_pic)

                 print(l)   
                 
                 return render(request, template2)



    

    "pass painting into context"
    context = {
        
        'form': form,
    }

    return render(request, template, context)


