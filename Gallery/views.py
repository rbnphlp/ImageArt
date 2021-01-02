from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Painting,Category
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

    paintings = Painting.objects.filter(Add_to_Gallery=True)
    query = None
    categories=None
    sort = None
    direction = None

    if request.GET:
            if 'sort' in request.GET:
                sortkey = request.GET['sort']
                sort = sortkey
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    paintings = paintings.annotate(lower_name=Lower('name'))
                if sortkey == 'category':
                    sortkey = 'category__name'
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        sortkey = f'-{sortkey}'
                paintings = paintings.order_by(sortkey)

            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                print(categories)
                paintings = paintings.filter(category__name__in=categories)
                print(paintings)
                categories = Category.objects.filter(name__in=categories)


            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('paintings'))
                
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                paintings = paintings.filter(queries)

    current_sorting = f'{sort}_{direction}'  

    context = {
        'paintings': paintings,
        'search_term': query,
         'current_categories': categories,
         'current_sorting': current_sorting,
         
    }

    return render(request, 'Gallery/gallery.html', context)

    


def product_detail(request, painting_id):
    """ A view to show individual product/painting details """
    print(painting_id)

    product = get_object_or_404(Painting, pk=painting_id)

    context = {
        'product': product,
    }

    return render(request, 'Gallery/product_detail.html', context)



@login_required
def add_painting(request):
    """ Add a product to the store """
    form = PaintingForm()
    
    template = 'Gallery/add_painting.html'
    template2 = 'Gallery/painting_no_gallery.html'
    template3 ='Gallery/painting_price_form.html'

    

    "if add to gallery is not checked , simply process the images and output to html , else  save each image  and generate a different template" 
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        print("In request post")
        if form.is_valid():
            "check if add to gallery is not added  and simply render no saving images"
            add_to_gallery=form.cleaned_data['Add_to_Gallery']
            print(add_to_gallery)
           
            "Get save "
            form.save()
            
            content_path=MEDIA_ROOT+'/'+'Gallery_images/Upload_pic/'+request.FILES['upload_pic'].name
            style_path=MEDIA_ROOT+'/'+'Gallery_images/Style_pic/'+request.FILES['style_pic'].name
            upload_image=load_img(content_path)
            style_image=load_img(style_path)
            stylized_image = hub_model(tf.constant(upload_image), tf.constant(style_image))[0]
            l=tensor_to_image(stylized_image)

            "Save the painitng"
            url_painting=MEDIA_ROOT+'/'+'Gallery_images/Paintings/'+request.FILES['upload_pic'].name
            displayurl=MEDIA_URL+'Gallery_images/Paintings/'+request.FILES['upload_pic'].name
            "resize Image"
            l= l.resize((new_width, new_height), PIL.Image.ANTIALIAS)
            l.save(url_painting)
            if not add_to_gallery :
                

                # Resize image     
                 
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

                combined_image_save=MEDIA_ROOT+'/'+'Gallery_images/Upload_style_combined/'+upload_name+"_"+style_name
                display_combinedurl=MEDIA_URL+'Gallery_images/Upload_style_combined/'+upload_name+"_"+style_name   
                "Save in form for combined image" 
                combined_image.save(combined_image_save)


                
                saved_form.image=displayurl
                saved_form.upload_style_combined=display_combinedurl
                saved_form.save()

                "Take the user to add name description and rating"
                context={
                   
                    'form_with_painting': saved_form,
                    'stylised_painting' : displayurl

                }

                return redirect('paintings')    


    

    "pass painting into context"
    context = {
        
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_painting(request, painting_id):



    """ Edit a product in the store """
    product = get_object_or_404(Painting, pk=painting_id)
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = PaintingForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'Gallery/edit_painting.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_painting(request, painting_id):
    """ Delete a product from the store """
    product = get_object_or_404(Painting, pk=painting_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('paintings'))