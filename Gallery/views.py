from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Painting
from .forms import PaintingForm
from utils.style_transfer import * 
from ImageArt.settings import MEDIA_ROOT,MEDIA_URL
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
# Create your views here.

"dimesnions for painting"
new_width  = 380
new_height = 512

hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
                 

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
           
            "Get save "
            
            content_path=MEDIA_ROOT+'/'+'Gallery_images/Upload_pic/'+request.FILES['upload_pic'].name
            style_path=MEDIA_ROOT+'/'+'Gallery_images/Style_pic/'+request.FILES['style_pic'].name
            upload_image=load_img(content_path)
            style_image=load_img(style_path)
            stylized_image = hub_model(tf.constant(upload_image), tf.constant(style_image))[0]
            l=tensor_to_image(stylized_image)
            if not add_to_gallery :
                

                # Resize image     
                 url_painting=MEDIA_ROOT+'/'+'Gallery_images/Paintings/'+request.FILES['upload_pic'].name
                 displayurl=MEDIA_URL+'Gallery_images/Paintings/'+request.FILES['upload_pic'].name
                 l.save(url_painting)
                 context = {
        
                        'stylised_painting': displayurl,
                    }

                 return render(request, template2,context)
            else: 
                print("IN add Gallery")
                " process the  files  and render "
                saved_form=form.save()
                "Combine style and upload image"
                content_image_pil = PIL.Image.open(content_path)
                style_image_pil = PIL.Image.open(style_path)
                "Combine the image and save image url "
                combined_image=get_concat_v_resize(content_image_pil, style_image_pil, resize_big_image=False)
                combined_image=combined_image.resize((new_width, new_height), PIL.Image.ANTIALIAS)
                upload_name=request.FILES['upload_pic'].name
                upload_name=upload_name.split(".")[0]
                style_name=request.FILES['style_pic'].name

                saved_form.name=upload_name+"with"+style_name

                saved_form.save()
                combined_image_save=MEDIA_ROOT+'/'+'Gallery_images/Upload_style_combined/'+upload_name+"_"+style_name
                display_combinedurl=MEDIA_URL+'Gallery_images/Upload_style_combined/'+upload_name+"_"+style_name   
                "Save in form for combined image" 
                combined_image.save(combined_image_save)



    

    "pass painting into context"
    context = {
        
        'form': form,
    }

    return render(request, template, context)


